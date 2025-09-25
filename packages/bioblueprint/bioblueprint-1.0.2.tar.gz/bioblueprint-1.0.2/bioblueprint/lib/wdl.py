#! /usr/bin/env python3

import os
import re
import WDL
import logging
import networkx as nx
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)


def parse_expr_apply(expr, parsed_expr):
    """Parse a WDL function applied to an expression"""
    # extract the function and prepare a dictionary for argument population
    apply_dict = {"func": expr.function_name, "args": []}
    for arg in expr.arguments:
        apply_dict["args"].append(parse_expr(arg, []))
    parsed_expr.append(apply_dict)
    return parsed_expr


def parse_expr_array(expr, parsed_expr):
    for item in expr.items:
        parsed_expr.append(parse_expr(item, []))
    return parsed_expr


def parse_expr_get(expr, parsed_expr):
    parsed_expr = parse_expr(expr.expr, parsed_expr)
    return parsed_expr


def parse_expr_ident(expr, parsed_expr):
    parsed_expr.append(str(expr.name))
    return parsed_expr


def parse_expr_string(expr, parsed_expr):
    """Extract a Python str from a WDL String while removing extraneous quotes"""
    deconstruction = "".join(
        [x for x in expr.parts if x.replace("'", "").replace('"', "")]
    )
    parsed_expr.append(deconstruction)
    return parsed_expr


def parse_expr_value(expr, parsed_expr):
    parsed_expr.append(expr.value)
    return parsed_expr


def parse_expr_map(expr, parsed_expr):
    for k, v in expr.items:
        parsed_expr.append([parse_expr(k, []), parse_expr(v, [])])
    return parsed_expr


def parse_expr(expr, parsed_expr):
    """Recrusively parse expression types"""
    if isinstance(expr, WDL.Expr.Apply):
        parsed_expr = parse_expr_apply(expr, parsed_expr)
    elif isinstance(expr, WDL.Expr.Get):
        parsed_expr = parse_expr_get(expr, parsed_expr)
    elif isinstance(expr, WDL.Expr.Ident):
        parsed_expr = parse_expr_ident(expr, parsed_expr)
    elif isinstance(expr, WDL.Expr.String):
        parsed_expr = parse_expr_string(expr, parsed_expr)
    elif isinstance(expr, WDL.Expr.Array):
        parsed_expr = parse_expr_array(expr, parsed_expr)
    elif isinstance(expr, (WDL.Expr.Int, WDL.Expr.Boolean, WDL.Expr.Float)):
        parsed_expr = parse_expr_value(expr, parsed_expr)
    elif isinstance(expr, (WDL.Expr.Map)):
        parsed_expr = parse_expr_map(expr, parsed_expr)
    else:
        # expression parsing function needs to be added
        raise AttributeError(f"unaccounted expression type: {type(expr)}; {str(expr)}")
    return parsed_expr


def parse_call(G, node, io_dict={}, source_callee=None, source_node=None):
    # acquire the inputs delivered to the call
    callee = node.callee
    callee_tag = (callee.digest, callee.name,)
    # acquire the source information from the call
    if isinstance(callee, WDL.Tree.Task) or isinstance(callee, WDL.Tree.Workflow):
        G.add_edge(source_callee, callee_tag)
        if source_node:
            derived_source = source_node + "." + node.name
        else:
            derived_source = node.name
        if isinstance(callee, WDL.Tree.Workflow):
            # recursively parse a workflow
            G, io_dict = parse_wf(G, callee, io_dict, callee_tag, derived_source)
            io_dict[derived_source] = {
                "callee": callee_tag,
                "inputs": populate_inputs(callee.inputs),
                "outputs": {x.name: str(x.type) for x in callee.outputs},
            }
        elif isinstance(callee, WDL.Tree.Task):
            io_dict[derived_source] = {
                "callee": callee_tag,
                "inputs": populate_inputs(callee.inputs),
                "outputs": {x.name: str(x.type) for x in callee.outputs},
            }
    else:
        raise AttributeError(f"unexpected call type {type(callee)}")
    return G, io_dict


def parse_scatter_condn(G, node, io_dict={}, source_callee=None, source_node=None):
    """Parse a scatter or conditional expression and append to graph and io_dict as tasks/wfs appear"""
    for node in node.body:
        if isinstance(node, WDL.Tree.Call):
            G, io_dict = parse_call(
                G, node, io_dict, source_callee=source_callee, source_node=source_node
            )
        elif isinstance(node, (WDL.Tree.Conditional, WDL.Tree.Scatter)):
            G, io_dict = parse_scatter_condn(
                G, node, io_dict, source_callee=source_callee, source_node=source_node
            )
        elif isinstance(node, WDL.Tree.Decl):
            continue  # these are just variable definitions, no action needed
        else:
            raise AttributeError(
                f"unexpected node type {type(node)} in scatter/conditional body"
            )
    return G, io_dict


def parse_wf(G, wf, io_dict={}, source_callee=None, source_node=None):
    """Obtain the necessary information from a WDL call node"""
    # parse the body of a workflow and compile its calls
    for node in wf.body:
        if isinstance(node, WDL.Tree.Call):
            G, io_dict = parse_call(
                G, node, io_dict, source_callee=source_callee, source_node=source_node
            )
        elif isinstance(node, (WDL.Tree.Conditional, WDL.Tree.Scatter)):
            G, io_dict = parse_scatter_condn(
                G, node, io_dict, source_callee=source_callee, source_node=source_node
            )
        elif isinstance(node, WDL.Tree.Decl):
            continue  # these are just variable definitions, no action needed
        else:
            raise AttributeError(f"unexpected node type {type(node)} in workflow body")
    return G, io_dict


def populate_inputs(inputs):
    """Populate the inputs dictionary with the name, type, and default values"""
    inputs_dict = {}
    for i in inputs:
        inputs_dict[i.name] = {"type": str(i.type), "default": None}
        if i.expr:
            data = [x for x in parse_expr(i.expr, [])]
            # only maintain the list type for Arrays/Maps
            if len(data) == 1:
                inputs_dict[i.name]["default"] = data[0]
            else:
                inputs_dict[i.name]["default"] = data
    return inputs_dict


def extract_inputs(inputs, source_inputs, dep_io_dict):
    """Extract default input data from dependencies and apply to source input dictionary"""
    inputs_dict = {}
    for node in inputs:
        # this is the source WDL
        if len(node.split(".")) == 1:
            inputs_dict[node] = source_inputs[node]
        # this is a downstream WDL
        else:
            node_data = re.search(r"(.*)\.([^\.]+$)", node)
            node_call = node_data.group(1)
            node_input = node_data.group(2)
            if node_call not in dep_io_dict:
                raise KeyError(
                    f"Node {node_call} not found in dependency I/O dictionary"
                )
            elif node_input not in dep_io_dict[node_call]["inputs"]:
                raise KeyError(
                    f"Input {node_input} not found in node {node_call} inputs"
                )
            inputs_dict[node] = {
                "type": dep_io_dict[node_call]["inputs"][node_input]["type"],
                "default": dep_io_dict[node_call]["inputs"][node_input]["default"],
            }
    return inputs_dict


def compile_workflow(workflow_file, G, dep_io_dict={}):
    """Import a WDL workflow, return its dependency graph, and I/O"""
    wdl = WDL.load(workflow_file)

    # if this is a workflow, parse the workflow
    if wdl.tasks:
        raise AttributeError(
            f"Anticipated workflow WDL file {workflow_file} contains tasks"
        )
    elif wdl.workflow:
        wf_tag = (wdl.workflow.digest, wdl.workflow.name,)
        logger.debug(f"Parsing {wdl.workflow.name}")
        wf_io_dict = {wf_tag: {"inputs": {}, "outputs": {}}}
        if wdl.workflow.inputs:
            wf_io_dict[wf_tag]["inputs"] = populate_inputs(
                wdl.workflow.inputs
            )
        if wdl.workflow.outputs:
            wf_io_dict[wf_tag]["outputs"] = {
                x.name: str(x.type) for x in wdl.workflow.outputs
            }
        if wf_tag not in G.nodes:
            G.add_node(wf_tag)
        G, dep_io_dict = parse_wf(G, wdl.workflow, dep_io_dict, wf_tag)
    else:
        raise AttributeError(
            f"Anticipated workflow WDL file {workflow_file} does not contain a workflow"
        )

    inputs = extract_inputs(
        WDL.values_to_json(wdl.workflow.available_inputs),
        wf_io_dict[wf_tag]["inputs"],
        dep_io_dict,
    )
    outputs = WDL.values_to_json(wdl.workflow.effective_outputs)

    return G, {"inputs": inputs, "outputs": outputs}, wf_tag


def extract_wdl_nodes(wdl_file):
    """Parse a WDL file and obtain the tasks/workflows contained"""
    node_names = []
    logger.debug(f"Parsing WDL file {wdl_file}")
    wdl = WDL.load(wdl_file)
    if wdl.workflow:
        wdl_tag = (wdl.workflow.digest, wdl.workflow.name,)
        node_names.append(wdl_tag)
    elif wdl.tasks:
        for task in wdl.tasks:
            node_names.append((task.digest, task.name,))
    else:
        raise AttributeError(
            f"Anticipated WDL file {wdl_file} does not contain a workflow or task"
        )
    return node_names


def get_wf_wdls(root_dir, prerepo, wf_prefix="wf_", wf_suffix=".wdl"):
    """Compile the WDL files in a directory and present their repo / full PATH for downstream parsing"""
    wf_data = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            # it is a workflow if it starts with prefix and ends with suffix
            # this could be a problem w/o wf-specific prefixes, and would thus require opening and evaluating if a workflow
            if filename.startswith(wf_prefix) and filename.endswith(wf_suffix):
                wf_data[full_path] = re.sub(r"^" + prerepo, "", full_path)
    return wf_data


def compile_repo(wf_dir, wf_prefix="wf_", wf_suffix=".wdl"):
    """Acquire all workflows and compile the repository's dependency graph"""
    # get the base repository path
    repo_base = os.path.abspath(wf_dir)
    if not repo_base.endswith("/"):
        repo_base = repo_base + "/"
    prerepo = os.path.dirname(repo_base) + "/"

    workflows = get_wf_wdls(wf_dir, prerepo, wf_prefix, wf_suffix)
    # initialize the graph
    G = nx.DiGraph()
    # init the io dict
    io = {}
    for path, repo_path in workflows.items():
        G, io_prep, wdl_tag = compile_workflow(path, G, {})
        io_prep['path'] = repo_path
        io[wdl_tag] = io_prep

    return G, {k: v for k, v in sorted(io.items(), key=lambda x: x[0])}