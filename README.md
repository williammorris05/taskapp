
----------------------------------------------------------------------
Setup & run
----------------------------------------------------------------------

## Inital setup of virtual enviroment Windows

- Open the the root of the project in windows file explorer (default called hugb-group-18-project)
- Right click the background in file explorer, which opens a drop-down menu.
- Select "open in terminal" in the dropdown menu.
- This opens Windows powershell, in there copy the command below, paste it in the terminal window and press enter

		python -m venv venv

- Then copy/paste this command

		.\venv\Scripts\Activate.ps1

- Then copy paste this command

		pip install -r requirements.txt

You have now set up the virtual environment.

-----------------------

## Initial setup of virtual environment — macOS

- Open the root of the project in Finder (default called hugb-group-18-project)
- Right click the background of the folder, which opens a drop-down menu.
- Select "New Terminal at Folder" in the dropdown menu.
  (If you don’t see this option, open the Terminal app manually and navigate to the project folder with: cd path/to/hugb-group-18-project)

- This opens a terminal window. Copy/paste the command below, press enter to create the virtual environment:

        python3 -m venv venv

- Then copy/paste this command to activate the environment:

        source venv/bin/activate

- Then copy/paste this command to install dependencies:

        pip install -r requirements.txt

You have now set up the virtual environment.

-----------------------

# How to run the server on Windows
If you have never created the virtual environment described above, do that first

- Open the the root of the project in windows file explorer (Folder called hugb-group-18-project)
- Right click the background, which opens a drop-down menu.
- Select "open in terminal" in the dropdown menu.
This opens Windows powershell.

- You should see (venv) in front of the command line if it the virtual environment active
 If the venv is not active, activate it with the command
		
		.\venv\Scripts\Activate.ps1
- With the venv active, copy/paste this command into the terminal
		
		 flask --app 'src\app\server' run
     
The server is now running on the URL http://127.0.0.1:5000

1) Create and activate a virtualenv

macOS/Linux
  python3 -m venv venv
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

-----------------------

# How to run the server on macOS
If you have never created the virtual environment described above, do that first.

- Open the root of the project in Finder (Folder called hugb-group-18-project)
- Right click the background, which opens a drop-down menu.
- Select "New Terminal at Folder" in the dropdown menu.
  (Or manually open the Terminal app and navigate with: cd path/to/hugb-group-18-project)

- You should see (venv) in front of the command line if the virtual environment is active.
  If the venv is not active, activate it with the command:

        source venv/bin/activate

- With the venv active, copy/paste this command into the terminal:

        flask --app 'src/app/server.py' run

The server is now running on the URL http://127.0.0.1:5000

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

