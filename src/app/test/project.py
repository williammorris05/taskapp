import unittest
from src.app.models.project import Project

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


if __name__ == "__main__":
    unittest.main()
