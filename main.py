from fastapi import FastAPI
from op import * 

app = FastAPI()
create_table()

@app.post("/login" )
def login(email,password):

    user = login_user(email,password)
    # if user: 
    #     return app.status.HTTP_200_OK 


@app.post("/register")
def registr_api(email: str, password: str):
    register(email, password)
    return {"status": "user added"}

@app.get("/tasks")
def get_all_tasks():
    return show_all_tasks()

# @app.get("/tasks/completed")
# def get_completed_tasks():
#     return show_completed()

@app.get("/tasks/incomplete")
def get_incomplete_tasks():
    return show_not_comleted()

@app.post("/tasks")
def create_task(task: str, user_id):
    add_task(task, user_id)
    return {"status": "task added", "task": task}

@app.put("/tasks/{task_id}")
def mark_task_done(task_id: int):
    update_task_status(task_id)
    return {"status": "task updated", "id": task_id}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    delete_tasks(task_id)
    return {"status": "task deleted", "id": task_id}

if __name__ == "__main__":
   import uvicorn
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)