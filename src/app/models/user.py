"""User model: stub for Sprint 2; fleshed out in later sprints."""
from dataclasses import dataclass


@dataclass
class User:
    userId: str
    name: str
    email: str = ""
