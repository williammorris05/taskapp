
"""Task model: minimal shape for Sprint 2 demo and tests."""


from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    taskId: str
    title: str
    status: str = "open"
    priority: str = "Normal"
    createdAt: str = date.today().isoformat()
    projectParent: str = ""
    description: str = ""
    deadline: str = ""   # optional, ISO date string
