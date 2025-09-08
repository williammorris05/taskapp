# Decision protocol

- Decisions are made when a majority of the group is present and together.
- All code that is to be committed to the repository needs to be peer reviewed by another member of the group.
- If there are conflicting opinions on a decision, it will be solved through a poll on our groups discord channel.
- Simple decisions can be made by the person responsible, no need for peer review. *Naming variables, formatting, etc.*

---
# Project overview

**Chosen product:** Join & Do
Join & Do is a collaboration app where people can create, join and complete tasks together.
This will be developed in a few parts, this first one focusing on requirements and modelling.

---
## Stakeholders / Personas

### Our main users are:

- **Students** – want to study together, prepare for exams, and stay motivated.
- **Fitness enthusiasts** – want accountability partners for workouts and healthy goals.
- **Exchange students / newcomers** – want to connect socially while doing everyday tasks.
- **Young professionals** – want to collaborate on small work or personal goals.
- **General everyday users** – want motivation and companionship for chores, hobbies, or lifestyle goals.

### Why they would use Join & Do

Users are motivated to:

- Find partners for tasks they don’t want to do alone.
- Connect with others
- Organize and track tasks with groups.

---
## Scope

### In Scope

- **Account management**: users can sign up, log in, update their details, or delete their account
- **Profiles**: each user has a profile where basic info and points/progress are stored
- **Tasks**: users can create, edit, and delete tasks, and break them into subtasks
- **Groups**: people can create groups, join existing ones, and invite or remove members
- **Collaboration**: users can leave comments on tasks or subtasks

### Out of Scope

- **Frontend/UI development** (this project focuses only on backend/business logic)
- **Third-party integrations** (payments, calendar sync, social media login)
- **Advanced features** like smart recommendations, AI-based scheduling

---
## Functional Requirements

| Priority | Requirement
| - | - |
A | Log in
A | Register 
A | Edit account
A | Edit profile
A | Create a task
A | Edit a task
A | Close or remove a task
A | Create a group
A | Join a group
A | Invite a user to a group
A | Create a project
A | Join a project
A | Invite a group to a project
A | Assign a task to a project
A | Close or remove a task
B | Profiles
B | Set task priority
B | Categorize a task
B | Point acquisition
B | Achievements
B | Comments on tasks

---
### Scenarios

**Person:** Klara (20), female <br>
**Motivation:** Doesn’t want to study alone, wants a partner for motivation. <br>
**Story:** Klara logs into *Join & Do* and opens the task overview. She clicks *Create task*, gives it the title *“Study Calculus ”*, sets the *category* to *School* She creates two *subtasks*: *Read section 3-4* and *Solve practice problems*. She then presses create task and it appears on the site Join a group and collaborate

**Persona:** Aron (25), fitness enthusiast <br>
**Motivation:** Wants to stay motivated with fitness goals. <br>
**Story:** Aron signs up for *Join & Do* and searches for public groups. He finds a group called *“Morning Fitness Crew”* and clicks *Join group*. Inside, he sees ongoing tasks like *“Go for a 20 min run”* and *“Do 30 push-ups”*. He accepts the run task, marks it as *In progress*, and after attending it he marks it off as complete.

**Persona:** Simone (21), exchange student <br>
**Motivation:** Wants company and connection with new people <br>
**Story:** Simone is having problems with connecting with people in her exchange studies, she feels alone. She logs into *Join & Do* and browses the list of *open tasks* created by other users. She finds one called *“Weekly meal prep”*, created by another student living nearby. She clicks *Join task* and is automatically added to the creator’s group. Together, they agree on a time in and go together for grocery shopping and cooking. After completing the task, they both mark it as *Done*.

---
<br>
![Domain diagram image](https://gitlab.com/GiblerGoobler/hugb-group-18-project/-/raw/main/docs/sprint1/Sprint1_DomainDiagram.png)