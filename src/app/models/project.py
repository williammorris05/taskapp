from datetime import datetime


class Project:
    # Temporary for sprint 2 testing. Resets to 0 when program is closed
    IDCounter = 0

    def __init__(
        self,
        projectTitle: str,
        category: str,
        projectAdmin: str,
        status: str,
        dueDate: datetime
    ):
        """ Constructor for project """
        Project.IDCounter += 1
        self.projectTitle = projectTitle
        self.projectID = (f"P{Project.IDCounter}")
        self.category = category
        self.members = [projectAdmin]
        self.projectAdmin = projectAdmin
        self.status = status
        self.tasksList = []
        self.createdAt = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.dueDate = dueDate

    def __str__(self):
        """For testing purposes to see if class was made correctly"""
        return str(print(
            self.projectTitle,
            self.projectID,
            self.category,
            self.members,
            self.projectAdmin,
            self.status,
            self.tasksList,
            self.createdAt,
            self.dueDate
            ))

    def inviteToProject():
        pass


if __name__ == "__main__":
    CleanRoom = Project("Clean my room", "cleaning", "John", "Open", "AAA")
    print(CleanRoom)
