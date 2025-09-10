# Project overview

**Chosen product:** Join & Do <br>
***Join & Do*** is a collaboration app that enables people to create tasks and projects, join others, and work together to complete them
with gamification elements to keep things engaging.
The development will be divided into several phases, with the first phase **Sprint 1** focusing on eliciting requirements and creating
core models for the development of the software.

---
## Stakeholders

### Primary stakeholders:

- **Students** – who want to study with others and get ready for exams together.
- **Fitness enthusiasts** – seeking partners to stay consistent with workouts and lifestyle goals.
- **Exchange students / newcomers** –  who want to connect socially while doing everyday tasks.
- **Young professionals** – who want to collaborate on small work or personal goals.
- **General everyday users** – who want motivation and companionship for chores, hobbies, or lifestyle goals.

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
## Methods Used for Elicitation

To define the functionality of *Join & Do*, we used the following elicitation methods:

- **Brainstorming sessions**: We met as a group to discuss what features we wanted and what users should be able to do and how the program should function
- **Review of project documentation**:  We studied the course materials to understand the assignment and how we should work and what the expected outcome should be.
- **User story writing**: We transformed ideas into user stories in the format  
  *“As a [persona], I want [feature], so that [benefit]”*.  
- **Personas and scenarios**: We created fictional users (students, fitness enthusiasts, exchange students, etc.) and wrote scenarios to better imagine real usage situations.  
- **Peer discussion with TA**: We clarified uncertainties and validated that our requirements made sense for the course project.  

These methods led to the creation of our **functional requirements and user stories**, which we have registered as **GitLab issues under the “Open” label** to form our product backlog.


---
## Functional Requirements

| Priority | Requirement
| - | - |
A | Log in
A | Register 
A | Edit/Delete Account
A | View All Tasks and Projects
A | Create a Task
A | Edit Project
A | Remove Project as User
A | Invite to Project
A | Remove From Project
A | Overview of Finished Projects
A | Receive Notifications
A | View Tasks in Project
A | Profiles
A | Edit Profile
A | Create a Project
A | Join a Project
A | Assign a Task to a Project
A | Close or Remove a Task as User
B | Categorise Projects
B | Comment on Tasks
B | Set Task Priority
B | Point acquisition
B | Achievements
B | Remove Project as System Admin
B | Close or Remove a Task as System Admin
B | Delete Account as System Admin



---
### Scenarios

**Person:** Klara (20), female <br>
**Motivation:** Doesn’t want to study alone, wants a partner for motivation. <br>
**Story:** Klara logs into *Join & Do* and opens the task and project overview. She clicks *Create project*, gives it the title *“Study Calculus ”*, sets the *category* to *School* She creates two *tasks*: *Read section 3-4* and *Solve practice problems*. She then presses create task and it appears on the site Join a group and collaborate

**Persona:** Aron (25), fitness enthusiast <br>
**Motivation:** Wants to stay motivated with fitness goals. <br>
**Story:** Aron signs up for *Join & Do* and searches for public groups. He finds a group called *“Morning Fitness Crew”* and clicks *Join group*. Inside, he sees ongoing tasks like *“Go for a 20 min run”* and *“Do 30 push-ups”*. He accepts the run task, marks it as *In progress*, and after attending it he marks it off as complete.

**Persona:** Simone (21), exchange student <br>
**Motivation:** Wants company and connection with new people <br>
**Story:** Simone is having problems with connecting with people in her exchange studies, she feels alone. She logs into *Join & Do* and browses the list of *open projects* created by other users. She finds one called *“Weekly meal prep”*, created by another student living nearby. She clicks *Join project* and is automatically added to the creator’s group. Together, they agree on a time in and go together for grocery shopping and cooking. After completing the task, they both mark it as *Done*.

---
<br>
![Domain diagram image](https://gitlab.com/GiblerGoobler/hugb-group-18-project/-/raw/main/docs/sprint1/Sprint1_DomainDiagram.png)