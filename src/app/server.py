
"""Minimal Flask server exposing /task for Sprint 2 demo and tests."""

from flask import Flask, jsonify, request
from .interface import Interface
from flask import Response
import json


app = Flask(__name__)


@app.get('/')
def home():
    from flask import render_template
    return render_template('demo.html')


@app.route('/post_test', methods=['POST'])
def post_test():
    '''This is just to show how a POST request looks like; no functionality'''

    return '', 201


@app.route('/get_test', methods=['GET'])
def get_test():
    '''This is just a test to show how a GET request looks like'''
    return 'Hello World', 200


@app.route('/login', methods=['POST'])
def login():
    '''Put in a better docstring'''
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    if not username:
        return jsonify({"error": "Username cannot be empty"}), 400
    if not password:
        return jsonify({"error": "Password cannot be empty"}), 400
    try:
        # TODO return token?
        Interface.login(username, password)
        return jsonify({'msg': "Successfully logged in"}), 200
    # TODO, fill in correct errors
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/register', methods=['POST'])
def register():
    '''Put in a better docstring'''
    return '', 201


# Unsure of what route we'll have and the method used
@app.route("/invite", methods=["POST"])
def invite_route():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    if not username:
        return jsonify({"error": "Username cannot be empty"}), 400

    # Dummy logic for Sprint 2
    projectId = data.get("projectId", "p1")
    return jsonify({
        "message": f"Invited {username} to project {projectId}",
        "projectId": projectId,
        "user": username
    }), 200


@app.route("/task", methods=["POST"])
def task_route():
    # Accept empty body -> treat as {}
    data = request.get_json() or {}

    try:
        task = Interface.create_task(
            title=data.get("title", ""),
            description=data.get("description", ""),
            priority=data.get("priority", "Normal"),
            projectParent=data.get("projectParent", ""),
            deadline=data.get("deadline", "")
        )
        return jsonify(task), 201

    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400


@app.route("/project", methods=["POST"])
def project_route():
    data = request.get_json(silent=True) or {}
    # Minimal dummy response
    if not data.get("projectTitle"):
        return jsonify({"error": "Project title cannot be empty"}), 400

    project = {
        "projectId": "p1",  # hardcoded for Sprint 2
        "projectTitle": data["projectTitle"],
        "category": data.get("category", ""),
        "projectAdmin": data.get("projectAdmin", "u1"),
        "status": data.get("status", "open"),
        "dueDate": data.get("dueDate", ""),
        "members": [data.get("projectAdmin", "u1")]
    }
    return jsonify(project), 201


# ------------------------------------------------
# GET routes to fetch all tasks, projects, users
# ------------------------------------------------

@app.route("/tasks", methods=["GET"])
def get_tasks_route():
    tasks = Interface.get_all_tasks()
    return Response(
        json.dumps(tasks, indent=2, ensure_ascii=False),
        mimetype="application/json"
    )


@app.route("/projects", methods=["GET"])
def get_projects_route():
    projects = Interface.get_all_projects()
    return Response(
        json.dumps(projects, indent=2, ensure_ascii=False),
        mimetype="application/json"
    )


@app.route("/users", methods=["GET"])
def get_users_route():
    users = Interface.get_all_users()
    return Response(
        json.dumps(users, indent=2, ensure_ascii=False),
        mimetype="application/json"
    )
