"""Interface layer between Flask routes and business logic."""
from datetime import date
from .models.task import Task as TaskModel  # alias helps flake8


class Interface:
    @staticmethod
    def create_task(
        title: str,
        description: str = "",
        priority: str = "Normal",
        projectParent: str = "",
        deadline: str = ""
    ) -> TaskModel:
        """Create a TaskModel with minimal validation and dummy values."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = TaskModel(
            taskId="t1",  # hardcoded for Sprint 2
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            projectParent=projectParent,
            status="open",
            createdAt=date.today().isoformat(),
            deadline=deadline
        )
        return task
