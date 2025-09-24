import zntrack
import importlib.util
import uuid
import dataclasses
import typing as t
import zntrack
import networkx as nx
import inspect
from werkbank import ui_types as ut
import sys
import os
import typer
import json
from flask import jsonify
import contextlib
import io

app = typer.Typer()


class HandleType(t.TypedDict):
    id: str

class NodeData(t.TypedDict):
    label: str
    sourceHandles: list[HandleType]
    targetHandles: list[HandleType]

@dataclasses.dataclass(frozen=True)
class XYNode:
    """Class representing a node in the project graph.
    
    Example
    --------
    >>>       sourceHandles: [{ id: 'a-s-a' }, { id: 'a-s-b' }, { id: 'a-s-c' }],
      targetHandles: [],

    Resources
    ---------
    - https://reactflow.dev/docs/api/nodes/node/
    """
    id: str
    data: NodeData
    parentId: str | None
    type: t.Literal["Node", "Group"]


@dataclasses.dataclass(frozen=True)
class XYEdge:
    """Class representing an edge in the project graph.
    
    Example
    --------
    >>> {
    ... 'id': 'a-b',
    ... 'source': 'a',
    ... 'sourceHandle': 'a-s-a',
    ... 'target': 'b',
    ... 'targetHandle': 'a-t-b',
    ... }

    Resources
    ---------
    - https://reactflow.dev/examples/layout/elkjs-multiple-handles
    """
    id: str
    source: str
    sourceHandle: str
    target: str
    targetHandle: str

def get_project(path: str) -> zntrack.Project:
    """Import the zntrack project from the given path, ensuring CWD is in sys.path."""
    cwd = os.path.dirname(os.path.abspath(path))
    if cwd not in sys.path:
        sys.path.insert(0, cwd)
    spec = importlib.util.spec_from_file_location(uuid.uuid4().hex, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.project

def get_edges(project: zntrack.Project) -> list[XYEdge]:
    """Get the edges of the given project as a list of Edge dataclasses."""
    edges = []
    for edge in project.edges(data=True):
        a, b, data = edge
        a_name = project.nodes[a]["value"].name
        b_name = project.nodes[b]["value"].name
        edges.append(
            XYEdge(
                id=f"{a_name}-s-{data['u_attr']}-{b_name}-t-{data['v_attr']}",
                source=a_name,
                sourceHandle=f"{a_name}-s-{data['u_attr']}",
                target=b_name,
                targetHandle=f"{b_name}-t-{data['v_attr']}",
            )
        )
    return edges


def get_nodes(project: zntrack.Project) -> list[XYNode]:
    nodes = []
    # 1. create the groups as nodes
    for group in project.groups:
        group_name = "_".join(group)
        parent_id = None
        if len(group) > 1:
            parent_id = f"G.{'-'.join(group[:-1])}"
        nodes.append(
            XYNode(
                id=f"G.{group_name}",
                data={"label": group[-1], "sourceHandles": [], "targetHandles": []},
                parentId=parent_id,
                type="Group",
            )
        )
    # 2. sort nodes, such that parents always come before children
    # Topologically sort groups so that parents always come before children
    group_nodes = {node.id: node for node in nodes}
    group_graph = nx.DiGraph()
    for node in nodes:
        group_graph.add_node(node.id)
        if node.parentId is not None:
            group_graph.add_edge(node.parentId, node.id)
    sorted_group_ids = list(nx.topological_sort(group_graph))
    nodes = [group_nodes[group_id] for group_id in sorted_group_ids]

    # 3. create the actual nodes
    for node in project.nodes(data=True):
        node_id, data = node
        node: zntrack.Node = data["value"]
        parent_id = None
        if node.state.group:
            parent_id = f"G.{'_'.join(node.state.group.names)}"
        # get all incoming edges to determine the target handles
        v_attrs = {edge[2]["v_attr"] for edge in project.in_edges(node_id, data=True)}
        target_handles: list[HandleType] = [
            {"id": f"{node.name}-t-{v_attr}"} for v_attr in sorted(v_attrs)
        ]
        # get all outgoing edges to determine the source handles
        u_attrs = {edge[2]["u_attr"] for edge in project.out_edges(node_id, data=True)}
        source_handles: list[HandleType] = [
            {"id": f"{node.name}-s-{u_attr}"} for u_attr in sorted(u_attrs)
        ]
        nodes.append(
            XYNode(
                id=str(node.name),
                data={"label": str(node.name), "sourceHandles": source_handles, "targetHandles": target_handles},
                parentId=parent_id,
                type="Node",
            )
        )
    return nodes


def _get_node_info(node: zntrack.Node) -> tuple[str, bool]:
    """Extract documentation and deprecation status from a zntrack node."""
    docs = ""
    deprecated = False

    if hasattr(node.__class__, '__doc__') and node.__class__.__doc__:
        docs = node.__class__.__doc__.strip().split('\n')[0]  # First line only

    # Check if the class has a deprecated attribute or decorator
    if hasattr(node.__class__, '__deprecated__'):
        deprecated = node.__class__.__deprecated__

    return docs, deprecated

def _get_node_ports(project: zntrack.Project, node_id: str, node: zntrack.Node) -> list[ut.Port]:
    """Extract port information for a node."""
    ports = []

    # Get target ports from incoming edges (dependencies)
    v_attrs = {edge[2]["v_attr"] for edge in project.in_edges(node_id, data=True)}
    for v_attr in sorted(v_attrs):
        # Try to get type annotation
        annotation = "unknown"
        if hasattr(node.__class__, '__annotations__'):
            field_annotation = node.__class__.__annotations__.get(v_attr)
            if field_annotation:
                annotation = str(field_annotation).replace('typing.', '')

        ports.append(ut.Port(
            id=f"{node.name}-t-{v_attr}",
            type="target",
            category="dep",
            name=v_attr,
            annotation=annotation
        ))

    # Get source ports from outgoing edges (outputs)
    u_attrs = {edge[2]["u_attr"] for edge in project.out_edges(node_id, data=True)}
    for u_attr in sorted(u_attrs):
        # Try to get type annotation
        annotation = "unknown"
        if hasattr(node.__class__, '__annotations__'):
            field_annotation = node.__class__.__annotations__.get(u_attr)
            if field_annotation:
                annotation = str(field_annotation).replace('typing.', '')

        ports.append(ut.Port(
            id=f"{node.name}-s-{u_attr}",
            type="source",
            category="out",
            name=u_attr,
            annotation=annotation
        ))

    return ports

def _get_enhanced_nodes(project: zntrack.Project) -> list[ut.XYNode]:
    """Get nodes with enhanced data including ports, docs, and deprecation status."""
    nodes = []

    # 1. Create the groups as nodes
    for group in project.groups:
        group_name = "_".join(group)
        parent_id = None
        if len(group) > 1:
            parent_id = f"G.{'_'.join(group[:-1])}"
        nodes.append(ut.XYNode(
            id=f"G.{group_name}",
            data=ut.XYGroupData(label=group[-1]),
            parentId=parent_id,
            type="Group",
        ))

    # 2. Sort nodes, such that parents always come before children
    group_nodes = {node["id"]: node for node in nodes}
    group_graph = nx.DiGraph()
    for node in nodes:
        group_graph.add_node(node["id"])
        if node["parentId"] is not None:
            group_graph.add_edge(node["parentId"], node["id"])
    sorted_group_ids = list(nx.topological_sort(group_graph))
    nodes = [group_nodes[group_id] for group_id in sorted_group_ids]

    # 3. Create the actual nodes with enhanced data
    for node_data in project.nodes(data=True):
        node_id, data = node_data
        node: zntrack.Node = data["value"]
        parent_id = None
        if node.state.group:
            parent_id = f"G.{'_'.join(node.state.group.names)}"

        # Get node documentation and deprecation status
        docs, deprecated = _get_node_info(node)

        # Get port information
        ports = _get_node_ports(project, node_id, node)

        nodes.append(ut.XYNode(
            id=str(node.name),
            data=ut.XYNodeData(
                label=str(node.name),
                docs=docs,
                deprecated=deprecated,
                ports=ports,
                path=f"{node.__class__.__module__}.{node.__class__.__name__}"
            ),
            parentId=parent_id,
            type="Node",
        ))

    return nodes

def _get_enhanced_edges(project: zntrack.Project) -> list[ut.XYEdge]:
    """Get edges in the ut.XYEdge format."""
    edges = []
    for edge in project.edges(data=True):
        a, b, data = edge
        a_name = project.nodes[a]["value"].name
        b_name = project.nodes[b]["value"].name
        edges.append(
            ut.XYEdge(
                id=f"{a_name}-s-{data['u_attr']}-{b_name}-t-{data['v_attr']}",
                source=a_name,
                sourceHandle=f"{a_name}-s-{data['u_attr']}",
                target=b_name,
                targetHandle=f"{b_name}-t-{data['v_attr']}",
            )
        )
    return edges

def get_graph(project: zntrack.Project) -> dict[str, list[ut.XYNode] | list[ut.XYEdge]]:
    """Get the graph of the given project as a dictionary with nodes and edges."""
    return {"nodes": _get_enhanced_nodes(project), "edges": _get_enhanced_edges(project)}


@app.command()
def load_graph(path: str = "main.py"):
    """Load and print the graph of the zntrack project located at the given path."""
    print(">>> JSON")
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            project = get_project(path)
    except Exception:
        print(json.dumps({"error": "Unable to import project"}))
        sys.exit(1)
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            graph = get_graph(project)
    except Exception:
        print(json.dumps({"error": "Unable to extract graph"}))
        sys.exit(1)
    try:
        print(json.dumps(graph, default=dataclasses.asdict, indent=2))
    except Exception:
        print(json.dumps({"error": "Unable to serialize graph"}))
        sys.exit(1)

# def get_connections(project: zntrack.Project) -> dict:
#     """Get the connections of the given project as a dictionary."""
#     edges = {}

#     for edge in project.edges(data=True):
#         a, b, data = edge
#         a_name = project.nodes[a]["value"].name
#         b_name = project.nodes[b]["value"].name
#         if b_name not in edges:
#             edges[b_name] = {}
#         if data["v_attr"] not in edges[b_name]:
#             edges[b_name][data["v_attr"]] = []
#         edges[b_name][data["v_attr"]].append((a_name, data["u_attr"]))
#     return edges

# def get_connectivity(project: zntrack.Project) -> dict:
#     """Return a dict {node: [connected_nodes]} for all nodes in the project."""
#     connectivity = {}
#     for edge in project.edges(data=True):
#         a, b, _ = edge
#         a_name = project.nodes[a]["value"].name
#         b_name = project.nodes[b]["value"].name
#         if a_name not in connectivity:
#             connectivity[a_name] = []
#         connectivity[a_name].append(b_name)
#     return connectivity

# def get_nodes(project: zntrack.Project) -> dict:
#     """Get the nodes of the given project as a dictionary."""
#     nodes = {}
#     for node in project.nodes(data=True):
#         _, data = node
#         node = data["value"]
#         nodes[node.name] = {"module": node.__module__, "class": node.__class__.__name__}
#     return nodes

# def get_groups(project: zntrack.Project) -> dict:
#     """Get the groups of the given project as a dictionary."""
#     groups = {}
#     for names, nodes in project.groups.items():
#         current_level = groups
#         for name in names:
#             if name not in current_level:
#                 current_level[name] = {}
#             current_level = current_level[name]
#         # "." is never a valid group name, so we can use it
#         current_level["."] = [project.nodes[node]["value"].name for node in nodes]
#     return groups
