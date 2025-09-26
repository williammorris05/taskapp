"""Interface layer between Flask routes and business logic."""
# from datetime import date
from .models.task import TaskModel  # alias helps flake8
from .util import load_json
import os


class Interface:

    base_path = os.path.dirname(os.path.abspath(__file__))
    tasks = load_json(os.path.join(base_path, "data", "tasks.json"))
    projects = load_json(os.path.join(base_path, "data", "projects.json"))
    users = load_json(os.path.join(base_path, "data", "users.json"))

    @classmethod
    def get_all_tasks(cls):
        return cls.tasks

    @classmethod
    def get_all_projects(cls):
        return cls.projects

    @classmethod
    def get_all_users(cls):
        return cls.users

    @classmethod
    def create_task(cls, title, description="", priority="Normal",
                    projectParent="", deadline=""):
        task_id = f"t{len(cls.tasks) + 1}"
        task_obj = TaskModel(
            taskId=task_id,
            title=title,
            description=description,
            priority=priority,
            projectParent=projectParent,
            deadline=deadline
        )
        cls.tasks.append(task_obj.to_dict())
        return task_obj.to_dict()
