# Modern Software Engineering with DevOps

With this project I developed back end points that updates requests with JSON. I have listed the end point structure below. The functions consist of being able to create users and passwords, as well as create tasks for users to complete. App has two sub apps that work together. Using insomnia, all the end points can be tested and are working as expected. 

### Features
1. User registration and login.
2. Create Tasks that need to be done.
3. Assign user to task.
4. Mark tasks as completed and completed whowm.
5. Delete tasks and update tasks as needed.

### API End Points
#### Tasks
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | api/tasks/ |
| index | GET | api/tasks/ |
| Show | GET | api/tasks/{id}/ |
| Delete | DELETE | api/tasks/{id}/ |
| Update | PUT | api/tasks/{id}/ |

#### Users
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /users |
| index | GET | /users |
| Show | GET | /users/{id}/ |
| Delete | DELETE | /users/{id}/ |
| Update | PUT | /users{id}/ |
| Assignments | GET | /users/{id}/assignments/|

### DB Schema
1. users
    - user_id: pk
    - email
    - first name
    - last name
    - password
2. tasks
    - task id: pk
    - title
    - assigned_to
    - task_due_date
    - description
    - completed

