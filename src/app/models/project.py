from datetime import datetime


class Project:
    """ Base class for project """
    def __init__(
        self,
        projectTitle: str,
        category: str,
        projectAdmin: str,
        status: str,
        dueDate: datetime
    ):
        self.projectTitle = projectTitle  
        self.projectID = (f"P-HEREGOESID")
        self.category = category
        self.members = [projectAdmin]
        self.projectAdmin = projectAdmin
        self.status = status
        self.tasksList = []
        self.createdAt = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.dueDate = dueDate


if __name__ == "__main__":
