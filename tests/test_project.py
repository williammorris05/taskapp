import unittest
from app.models.project import Project


# How to run the tests
# individual tests python3 -m unittest src.app.test.project.TestProject.<function name>
# all tests python3 -m unittest src.app.test.project

EXISTING_USERS = ["John", "Tester"]


class TestProject(unittest.TestCase):
    """Failiure test
    This tests if a project with no title fails. If a project is created
    without a title, python raises type error and the test passes
    (it failed to create the project)"""

    def test_title_required(self):
        with self.assertRaises(TypeError):
            Project(
                category="cleaning",
                projectAdmin="John",
                status="Open",
                dueDate=None
            )
    """Tests that creating a project with a title succeeds and stores the
      correct title"""

    def test_title_given(self):
        p = Project(
            projectTitle="Clean room",
            category="cleaning",
            projectAdmin="John",
            status="Open",
            dueDate=None
        )
        self.assertEqual(p.projectTitle, "Clean room")

    def user_exists(self, username):
        return username in EXISTING_USERS

    """make sure a user exists before project is created"""

    def test_user_must_exist_before_project(self):
        user = "John"
        if not self.user_exists(user):
            self.fail(f"User '{user}' does not exist")

        p = Project(
            projectTitle="Clean room",
            category="cleaning",
            projectAdmin=user,
            status="Open"
        )
        self.assertEqual(p.projectAdmin, "John")

    """This tests inviting an existing user"""

    def test_invite_valid_user(self):
        user = "Tester"
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
