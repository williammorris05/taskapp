# How to Run and Use the Application

## 🚀 Run the Flask App

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   flask --app src/app/server run
   ```
   The app will start at:  
   👉 http://127.0.0.1:5000  

---

## 📬 Demo Requests in Postman

### 1. Create a Project
**POST** `/project`  
```json
{
  "projectTitle": "Clean Room",
  "category": "cleaning",
  "projectAdmin": "John"
}
```
👉 Creates a new project with the given name and description.  

---

### 2. Create a Task
**POST** `/task`  
```json
{
  "title": "Finish sprint",
  "description": "Implement create_task endpoint",
  "priority": "High",
  "projectParent": "p1",
  "deadline": "2025-10-01"
}
```
👉 Adds a new task to the specified project.  

---

### 3. Invite a User
**POST** `/invite`  
```json
{
  "username": "Tester",
  "projectId": "p1"
}
```
👉 Sends an invite to a user for the given project.  

---

## 🧪 Quick cURL Examples

```bash
# Create a project
curl -X POST http://127.0.0.1:5000/project   -H "Content-Type: application/json"   -d '{"name":"My First Project","description":"Demo project from Postman"}'

# Create a task
curl -X POST http://127.0.0.1:5000/task   -H "Content-Type: application/json"   -d '{"title":"Finish sprint","description":"Implement create_task endpoint","priority":"High","projectParent":"p1","deadline":"2025-10-01"}'

# Invite a user
curl -X POST http://127.0.0.1:5000/invite   -H "Content-Type: application/json"   -d '{"username":"Tester","projectId":"p1"}'
```