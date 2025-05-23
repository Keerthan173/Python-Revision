from pydantic import BaseModel      # Pydantic is used to validate the data

class Task(BaseModel):
    title: str
    description: str
    status: str
    
class TaskWithID(Task):     #Inherits from Task and adds an id (unique identifier for each task).
    id: int
    
class UpdateTask(BaseModel):    #All fields are optional (None), so you can update just one thing.
    title: str | None = None
    description: str | None = None
    status: str | None = None
