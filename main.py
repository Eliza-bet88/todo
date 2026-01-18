from fastapi import FastAPI
from op import (
    create_table,
    show_all_tasks,
    show_not_comleted,
    show_completed,
    add_task,
    update_task_status,
    delete_tasks,
)

app = FastAPI()
create_table()

@app.get("/tasks")
def get_all_tasks():
    return show_all_tasks()

@app.get("/tasks/completed")
def get_completed_tasks():
    return show_completed()

@app.get("/tasks/incomplete")
def get_incomplete_tasks():
    return show_not_comleted()

@app.post("/tasks")
def create_task(task: str):
    add_task(task)
    return {"status": "task added", "task": task}

@app.put("/tasks/{task_id}")
def mark_task_done(task_id: int):
    update_task_status(task_id)
    return {"status": "task updated", "id": task_id}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    delete_tasks(task_id)
    return {"status": "task deleted", "id": task_id}