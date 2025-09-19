import unittest
from src.app.models.project import Project

# How to run all tests at once
# python3 -m unittest src.app.test.test_project_invite

EXISTING_USERS = ["Maria", "Hannah", "Bob", "John"]


class TestProject(unittest.TestCase):
    def user_exists(self, username):
        return username in EXISTING_USERS

    """This tests inviting an existing user"""
    def test_invite_valid_user(self):
        user = "Maria"
        if not self.user_exists(user):
            self.fail(f"User '{user}' does not exist")

        p = Project(
                projectTitle="Clean room",
                category="cleaning",
                projectAdmin="John",
                status="Open",
                dueDate=None
            )
        self.assertIsInstance(p.inviteToProject(user, EXISTING_USERS), dict)
        self.assertIn(user, p.members)

    """Failure test
    This tests if inviting a nonexistent user fails"""
    def test_invite_nonexistent_user(self):
        user = "Sam"
        p = Project(
                projectTitle="Clean room",
                category="cleaning",
                projectAdmin="John",
                status="Open",
                dueDate=None
            )
        self.assertEqual(
            p.inviteToProject(user, EXISTING_USERS),
            "User does not exist"
            )
        self.assertNotIn(user, p.members)

    """Failure test
    This tests if inviting a user that is already a member fails"""
    def test_invite_already_member(self):
        user = "John"
        if not self.user_exists(user):
            self.fail(f"User '{user}' does not exist")
        p = Project(
                projectTitle="Clean room",
                category="cleaning",
                projectAdmin="John",
                status="Open",
                dueDate=None
            )
        self.assertEqual(
            p.inviteToProject(user, EXISTING_USERS),
            "User is already in the project"
            )
        self.assertEqual(p.members.count(user), 1)

    """Failure test
    This tests if inviting with no username fails"""
    def test_invite_empty_username(self):
        user = ""
        p = Project("Clean room", "cleaning", "John", "Open", "01-01-2026")
        result = p.inviteToProject(user, EXISTING_USERS)
        self.assertEqual(result, "User does not exist")
        self.assertNotIn(user, p.members)


if __name__ == "__main__":
    unittest.main()
