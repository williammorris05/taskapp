# Re-export models so you *can* import from app.models if you want.
from .task import TaskModel
from .project import Project
from .user import User

__all__ = ["TaskModel", "Project", "User"]
