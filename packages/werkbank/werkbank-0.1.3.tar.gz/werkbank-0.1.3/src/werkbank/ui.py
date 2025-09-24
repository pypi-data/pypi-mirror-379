from flask import Flask, send_from_directory
from werkbank.project import get_project, get_edges, get_nodes, get_graph
from werkbank.utils import get_node_info
import os

app = Flask(__name__)
# TODO, using threading we can't import the project, because znflow.DiGraph is not thread safe!
project = get_project("main.py")

@app.route("/")
def serve_react_app():
    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    return send_from_directory(static_folder, 'index.html')


@app.route("/api/edges")
def edges():
    # project = get_project("main.py")
    connections = get_edges(project)
    return connections

@app.route("/api/nodes")
def nodes():
    # project = get_project("main.py")
    nodes = get_nodes(project)
    return nodes

# @app.route("/api/groups")
# def groups():
#     # project = get_project("main.py")
#     groups = get_groups(project)
#     return groups

@app.route("/api/info/<node_name>")
def nodename_info(node_name):
    # get the module and class name from node_name
    node = None
    for _, data in project.nodes(data=True):
        if data["value"].name == node_name:
            node = data["value"]
            break
    if node is None:
        return {}
    module = node.__class__.__module__
    class_name = node.__class__.__name__
    node_info = get_node_info(module, class_name)
    return node_info
    # node_info = get_node_info(node_name)
    # return node_info

@app.route("/api/graph")
def get_graph_data():
    graph = get_graph(project)
    return graph

# Catch-all route for static files and SPA routing
@app.route('/<path:path>')
def serve_static_files(path):
    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    if path and os.path.exists(os.path.join(static_folder, path)):
        return send_from_directory(static_folder, path)
    else:
        # For SPA routing, serve index.html for unknown routes
        return send_from_directory(static_folder, 'index.html')


def main():
    """Entry point for the werkbank CLI command."""
    app.run(host='127.0.0.1', port=5000, debug=True)