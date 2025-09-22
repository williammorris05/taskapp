import pytest
from app.interface import Interface


def test_create_task_success_with_deadline():
    task = Interface.create_task(
        title="Finish assignment",
        description="Implement create_task endpoint",
        priority="High",
        projectParent="p1",
        deadline="2025-10-01"
    )

    assert task.taskId == "t1"
    assert task.title == "Finish assignment"
    assert task.description == "Implement create_task endpoint"
    assert task.priority == "High"
    assert task.projectParent == "p1"
    assert task.deadline == "2025-10-01"
    assert task.status == "open"
    assert task.createdAt  # should not be empty


def test_create_task_success_without_deadline():
    task = Interface.create_task("Clean sink")
    assert task.deadline == ""   # default when none is provided
    assert task.status == "open"


def test_create_task_empty_title():
    with pytest.raises(ValueError):
        Interface.create_task("")
