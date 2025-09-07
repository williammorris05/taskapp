# Decision protocol
- Decisions are made when a majority of the group is present and together.
- All code that is to be committed to the repository needs to be peer reviewed by another member of the group.
- If there are conflicting opinions on a decision, it will be solved through a poll on our groups discord channel.
- Simple decisions can be made by the person responsible, no need for peer review. *Naming variables, formatting, etc.*

# Project overview
Chosen product: Join & Do
Join & Do is a collaboration app where people can create, join and complete tasks together. 
This will be developed in a few parts, this first one focusing on requirements and modelling.


# Stakeholders / Personas


Our main users are:


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


## Functional Requirements

### Accounts
- (A) Log in  
- (A) Register  
- (A) Edit/Delete account  
- (B) Profiles  

### Task Management
- View all tasks  
- (A) Create task  
- (A) Join a task  
- (A) Edit task  
- (A) Remove task  
- (B) Set priority of a task  
- (B) Categorize tasks  
- (B) Subtasks  

### Collaboration
- (A) Create groups  
- (A) Invite users to a group  
- (A) Remove users from a group  
- (A) Join a group  

### Gamification
- (B) Earn points for completing tasks  

### Communication
- (B) Comment system for tasks and subtasks  
- (B) Notifications and reminders  

## User stories
- As a user I want to **log in**, so that I can find someone to do tasks with.  
- As a user I want to **register**, so I can use the software from my account.  
- As a user I want to **edit my account**, so that I can update it in case my information changes.  
- As a user I want to **view all tasks**, so I can browse tasks.  
- As a user I want to **create a task**, so that I can find someone to do it with me.  
- As a user I want to **edit a task**, so if something changes I can update the task.  
- As a user I want to **remove tasks**, so if I don’t want to do it anymore it is deleted.  
- As a user I want to **create groups with people**, so that I can collaborate with them.  
- As a user I want to **invite other users to the group**, so that I can collaborate with them.  
- As a user I want to **remove another user from the group**, so they are not in the group.  
- As a user I want to **join another group**, so I can do tasks with said group.  
- As a user I want to **see an overview of finished tasks**, so that I can keep track of my past tasks.  
- As a user I want to **collect points when finishing a task**, so I feel a sense of accomplishment.  
- As a user I want to **message other users**, so we can communicate.  
- As a user I want to **comment on tasks/subtasks**, so I can add clarification.  
- As a user I want to **receive notifications**, so I can have reminders about tasks.  
- As a user I want to **categorize available tasks**, so I can find a task within my desired category.  
- As a user I want to **see subtasks**, so I can see everything included in the task.  
- As a user I want to **see other profiles**, so I can learn more about my task buddies.  
-As a user I want to **join an existing task**, so I can do it with another person


# Scenarios


 Create task
**Person:** Klara (20), female
**Motivation:** Doesn’t want to study alone, wants a partner for motivation.  


**Story:**  
Klara logs into *Join & Do* and opens the task overview. She clicks **Create task**, gives it the title **“Study Calculus ”**, sets the **category** to *School* She creates two **subtasks**: *Read section 3-4* and *Solve practice problems*.  
She then presses create task and it appears on the site


Join a group and collaborate
**Persona:** Aron (25), fitness enthusiast
**Motivation:** Wants to stay motivated with fitness goals.  


**Story:**  
Aron signs up for *Join & Do* and searches for public groups. He finds a group called **“Morning Fitness Crew”** and clicks **Join group**. Inside, he sees ongoing tasks like *“Go for a 20 min run”* and *“Do 30 push-ups”*.  
He accepts the run task, marks it as **In progress**, and after attending it he marks it off as complete.


**Persona:** Simone (21), exchange student  
**Motivation:** Wants company and connection with new people


**Story:**  
Simone is having problems with connecting with people in her exchange studies, she feels alone. She logs into *Join & Do* and browses the list of **open tasks** created by other users. She finds one called **“Weekly meal prep”**, created by another student living nearby.  
She clicks **Join task** and is automatically added to the creator’s group. Together, they agree on a time in and go together for grocery shopping and cooking. After completing the task, they both mark it as **Done**.



# Domain-model

# Project journal
