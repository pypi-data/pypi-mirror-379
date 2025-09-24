from flask import Flask, send_from_directory
from werkbank.project import get_project, get_edges, get_nodes, get_graph
from werkbank.utils import get_node_info
import os
import subprocess
import json

app = Flask(__name__)

@app.route("/")
def serve_react_app():
    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    return send_from_directory(static_folder, 'index.html')


@app.route("/api/graph")
def get_graph_data():
    # run werkbank-utils and load the stdout as json
    result = subprocess.run(["werkbank-utils", "--path", "main.py"], capture_output=True, text=True)
    # remove everything until ">>> JSON" line and then read the rest as json
    output = result.stdout
    json_str = output.split(">>> JSON")[1]
    graph = json.loads(json_str)
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