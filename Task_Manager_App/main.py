from fastapi import FastAPI, HTTPException
from operations import read_all_tasks, read_task , get_next_id , write_task_into_csv , create_tasks
from models import Task, TaskWithID, UpdateTask

app = FastAPI()     # Creates an instance of the FastAPI class.

@app.get("/tasks", response_model=list[TaskWithID])
def get_all_tasks():
    tasks = read_all_tasks()        #Reads all tasks from the CSV file.
    return tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    task = read_task(task_id)        #Reads a specific task by ID.
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

@app.post("/tasks", response_model=TaskWithID)
# response_model=TaskWithID: It means:
# The response (output) will be in the format of the TaskWithID model.
# That is: the user will see id, title, description, and status.
def add_task(task:Task):        # input: task of type Task.
    return create_tasks(task)


# @app.put("/tasks/{task_id}", response_model=TaskWithID)
# def update_task(task_id:int, task_update: UpdatedTask):
    