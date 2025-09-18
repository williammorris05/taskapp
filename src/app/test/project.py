import unittest
from src.app.models.project import Project

# How to run the tests
# python3 -m unittest src.app.test.project.<function_name>


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


if __name__ == "__main__":
    unittest.main()
