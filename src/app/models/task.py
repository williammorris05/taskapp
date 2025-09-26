
"""Task model: minimal shape for Sprint 2 demo and tests."""


# from dataclasses import dataclass
from datetime import date


class TaskModel:
    def __init__(self, taskId, title, description="", priority="Normal",
                 projectParent="", status="open", createdAt=None,
                 deadline=""):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        self.taskId = taskId
        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.projectParent = projectParent
        self.status = status
        self.createdAt = createdAt or date.today().isoformat()
        self.deadline = deadline

    def to_dict(self):
        return {
            "taskId": self.taskId,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "projectParent": self.projectParent,
            "status": self.status,
            "createdAt": self.createdAt,
            "deadline": self.deadline
        }
