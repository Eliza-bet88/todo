from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models.database import get_db, create_tables
from controllers.user_controller import UserController
from controllers.task_controller import TaskController

from pydantic import BaseModel
app = FastAPI()

create_tables()

class UserRegister(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class TaskCreate(BaseModel):
    task: str
    user_id: int

@app.post("/register")
def register(user_data: UserRegister, session: Session = Depends(get_db)):
    user = UserController().register_user(session, user_data.email, user_data.password)
    if user:
        return {
            "status": "success",
            "message": "User registered",
            "user_id": user.id,
            "email": user.email
        }
    else:
        return {"status": "error", "message": "User already exists"}

@app.post("/login")
def login(user_data: UserLogin, session: Session = Depends(get_db)):
    user = UserController().login_user(session, user_data.email, user_data.password)
    if user:
        return {
            "status": "success",
            "message": "Login successful",
            "user_id": user.id,
            "email": user.email
        }
    else:
        return {"status": "error", "message": "Invalid email or password"}

@app.post("/tasks")
def create_task(task_data: TaskCreate, session: Session = Depends(get_db)):
    task = TaskController().create_task(session, task_data.task, task_data.user_id)
    return {
        "status": "success",
        "task_id": task.id,
        "task": task.task,
        "status": task.status
    }

@app.get("/tasks")
def get_tasks(session: Session = Depends(get_db)):
    tasks = TaskController().get_all_tasks(session)
    return {
        "status": "success",
        "tasks": [
            {
                "id": current_task.id,
                "task": current_task.task,
                "status": current_task.status,
                "user_id": current_task.user_id
            }
            for current_task in tasks
        ]
    }

@app.get("/tasks/incomplete")
def get_incomplete(session: Session = Depends(get_db)):
    tasks = TaskController().get_incomplete_tasks(session)
    return {
        "status": "success",
        "tasks": [
            {
                "id": current_task.id,
                "task": current_task.task,
                "user_id": current_task.user_id
            }
            for current_task in tasks
        ]
    }

@app.get("/tasks/user/{user_id}")
def get_user_tasks(user_id: int, session: Session = Depends(get_db)):
    tasks = TaskController().get_user_tasks(session, user_id)
    return {
        "status": "success",
        "tasks": [
            {
                "id": current_task.id,
                "task": current_task.task,
                "status": current_task.status
            }
            for current_task in tasks
        ]
    }
@app.put("/tasks/{task_id}")
def mark_done(task_id: int, session: Session = Depends(get_db)):
    task = TaskController().mark_task_done(session, task_id)
    if task:
        return {
            "status": "success",
            "message": "Task marked as completed",
            "task_id": task.id
        }
    else:
        return {"status": "error", "message": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_db)):
    result = TaskController().delete_task(session, task_id)
    if result:
        return {
            "status": "success",
            "message": "Task deleted",
            "task_id": task_id
        }
    else:
        return {"status": "error", "message": "Task not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)