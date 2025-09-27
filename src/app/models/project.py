from datetime import datetime
from typing import Optional, List
import json


def next_project_id(path="projects.json"):
    """Helper to generate the next free projectId based on DB contents."""
    try:
        with open(path) as f:
            data = json.load(f)
        ids = [int(p["projectId"][1:]) for p in data["Projects"]]
        return f"p{max(ids) + 1}" if ids else "p1"
    except FileNotFoundError:
        return "p1"


class Project:
    # Temporary for sprint 2 testing. Resets to 0 when program is closed
    IDCounter = 0

    def __init__(
        self,
        projectTitle: str,
        category: str,
        projectAdmin,
        status: str,
        dueDate: Optional[str] = None,
        projectId: Optional[str] = None,
        members: Optional[List[str]] = None,
        tasksList: Optional[List[str]] = None,
        createdAt: Optional[str] = None

    ):
        """constructor for project made compatible with json database"""
        if projectId is None:
            projectId = next_project_id()

        self.projectTitle = projectTitle
        self.projectId = projectId
        self.category = category

        self.projectAdmin = projectAdmin

        self.members = members if members is not None else [projectAdmin]
        self.status = status
        self.tasksList = tasksList if tasksList is not None else []

        self.createdAt = createdAt or datetime.now().strftime("%d.%m.%y")
        self.dueDate = dueDate

    def __str__(self):
        """For testing purposes to see if class was made correctly"""
        return str((
            self.projectTitle,
            self.projectId,
            self.category,
            self.members,
            self.projectAdmin,
            self.status,
            self.tasksList,
            self.createdAt,
            self.dueDate
        ))

    def inviteToProject(self, username: str, usersList: list):
        """check if username exists"""
        if username not in usersList:
            return ("User does not exist")

        """check if username is already a member"""
        if username in self.members:
            return ("User is already in the project")

        """add user to the project"""
        self.members.append(username)
        return {"success! Members": self.members}

    def editProject(
            self,
            projectTitle=None,
            category=None,
            status=None,
            dueDate=None
    ):
        """Edit only the fields you pass in; leaves others unchanged."""
        if projectTitle is not None:
            if projectTitle.strip() == "":
                return "Project title cannot be empty"
            self.projectTitle = projectTitle
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if dueDate is not None:
            self.dueDate = dueDate

    def to_dict(self):
        return {
           "projectId": self.projectId,
           "projectTitle": self.projectTitle,
           "category": self.category,
           "members": self.members,
           "projectAdmin": [self.projectAdmin],
           "tasksList": self.tasksList,
           "createdAt": self.createdAt,
           "dueDate": self.dueDate
        }
# TODO: Check how we handle projectAdmin, is it user id?

    @classmethod
    def from_dict(cls, d):
        """Build Project from JSON record (unwrap admin list)."""
        admin = d.get("projectAdmin")
        if isinstance(admin, list):
            admin = admin[0] if admin else ""
        return cls(
            projectTitle=d.get("projectTitle", "Untitled"),
            projectId=d["projectId"],
            category=d["category"],
            projectAdmin=admin,
            status=d["status"],
            dueDate=d.get("dueDate"),
            members=d.get("members", []),
            tasksList=d.get("tasksList", []),
            createdAt=d.get("createdAt")
        )


if __name__ == "__main__":
    DB = "src/app/data/projects.json"

    with open(DB) as f:
        data = json.load(f)

    projects = [Project.from_dict(p) for p in data["Projects"]]

    for pr in projects:
        print(pr)
# CleanRoom = Project("Clean my room", "cleaning", "John", "Open")
# print(CleanRoom)
# EXISTING_USERS = ["Maria", "Hannah", "Bob", "John"]
# print(CleanRoom.inviteToProject("Bob", EXISTING_USERS))
