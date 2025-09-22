Group 18 — Sprint 2 (Minimal API + Tests)

Goal: clean, simple, demoable endpoints with tests and coverage.
Scope: no database, dummy/hardcoded IDs, minimal validation.
Note: Per Sprint 2 instructions, we exclude server.py from coverage.

----------------------------------------------------------------------
What’s implemented
----------------------------------------------------------------------
- POST /task — create task (201)
- POST /project — create project (dummy, 201)
- POST /invite — invite user to project (dummy, 200)
- Unit + route tests with coverage (≥ 50%)
- Clear separation: models → interface → server

----------------------------------------------------------------------
Requirements
----------------------------------------------------------------------
See requirements.txt:
Flask==3.0.3
pytest==8.4.2
pytest-cov==7.0.0

----------------------------------------------------------------------
Project structure
----------------------------------------------------------------------
src/
  app/
    __init__.py
    server.py            # Flask routes (/task, /project, /invite)
    interface.py         # Interface layer (create_task)
    models/
      __init__.py
      task.py            # Task dataclass (dummy defaults)
      project.py         # Project stub dataclass
      user.py            # User stub dataclass
tests/
  ...                    # pytest tests for logic + routes
pytest.ini               # pythonpath=src + coverage flags
requirements.txt
README.md

----------------------------------------------------------------------
Setup & run
----------------------------------------------------------------------

1) Create and activate a virtualenv

macOS/Linux
  python -m venv venv
  source venv/bin/activate

Windows (PowerShell)
  python -m venv venv
  .\venv\Scripts\Activate.ps1

2) Install dependencies
  pip install -r requirements.txt

3) Run tests (with coverage)
  pytest -v
  # or quiet:
  pytest

Coverage policy (Sprint 2): we do not count server.py. This is enforced via pytest.ini (see below).

4) Run the server (dev) – ENV VAR METHOD (recommended)

Run these from the project root (the folder that contains `src/`).

macOS/Linux (bash/zsh)
  export PYTHONPATH=src
  export FLASK_APP=app.server:app
  export FLASK_DEBUG=1
  flask run

Windows (PowerShell)
  $env:PYTHONPATH="src"
  $env:FLASK_APP="app.server:app"
  $env:FLASK_DEBUG="1"
  flask run

Tip: env vars apply to the current terminal session. If you open a new terminal, set them again—or add a `.env` file with:
  PYTHONPATH=src
  FLASK_APP=app.server:app
  FLASK_DEBUG=1
(If python-dotenv is installed, Flask will auto-load .env so plain `flask run` works.)

Server starts at: http://127.0.0.1:5000/

----------------------------------------------------------------------
Postman examples
----------------------------------------------------------------------

1) Create Task — POST /task (201)
Body:
{
  "title": "Finish sprint",
  "description": "Implement create_task endpoint",
  "priority": "High",
  "projectParent": "p1",
  "deadline": "2025-10-01"
}
Sample response:
{
  "taskId": "t1",
  "title": "Finish sprint",
  "status": "open",
  "priority": "High",
  "createdAt": "YYYY-MM-DD",
  "projectParent": "p1",
  "description": "Implement create_task endpoint",
  "deadline": "2025-10-01"
}

2) Create Project — POST /project (201)
Body:
{
  "projectTitle": "Clean Room",
  "category": "cleaning",
  "projectAdmin": "John"
}
Sample response (dummy):
{
  "projectId": "p1",
  "projectTitle": "Clean Room",
  "category": "cleaning",
  "projectAdmin": "John",
  "status": "open",
  "dueDate": "",
  "members": ["John"]
}

3) Invite User — POST /invite (200)
Body:
{
  "username": "Tester",
  "projectId": "p1"
}
Sample response (dummy):
{
  "message": "Invited Tester to project p1",
  "projectId": "p1",
  "user": "Tester"
}

Negative cases to demo
- /task with {"title": ""} → 400 {"error": "Task title cannot be empty"}
- /project with {} → 400 {"error": "Project title cannot be empty"}
- /invite with {"username": ""} → 400 {"error": "Username cannot be empty"}

----------------------------------------------------------------------
Pytest / coverage config
----------------------------------------------------------------------

pytest.ini (placed at repo root):
[pytest]
pythonpath = src
testpaths = tests
addopts = -q --cov=src/app --cov-report=term-missing --cov-fail-under=50

[coverage:run]
# Per Sprint 2: exclude the Flask wiring from coverage
omit =
    src/app/server.py

(Optional) If you need to exclude additional stubs, add them under `omit`.

----------------------------------------------------------------------
Housekeeping
----------------------------------------------------------------------

.gitignore:
venv/
__pycache__/
.pytest_cache/
.DS_Store

----------------------------------------------------------------------
Design notes (Sprint 2 constraints)
----------------------------------------------------------------------

- No persistence (no DB). Endpoints return dummy objects.
- IDs are hardcoded (t1, p1, u1) for demo consistency.
- Minimal validation:
  - /task: requires title (non-empty after strip)
  - /project: requires projectTitle
  - /invite: requires username
- Layered structure matches course style: models → interface → server.
- Tests cover both logic and HTTP routes; server.py excluded from coverage per sprint rules.

----------------------------------------------------------------------
Acknowledgements
----------------------------------------------------------------------

We used AI assistance to simplify and clarify the minimal implementation (as allowed by course policy). All team members understand the code paths we’re submitting and can explain each piece during review.
