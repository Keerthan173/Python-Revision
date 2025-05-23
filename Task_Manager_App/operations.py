import csv
from models import Task,TaskWithID, UpdateTask

DATABASE_FILENAME = "tasks.csv"
column_fields = ["id", "title", "description", "status"]        #These are the CSV column headers.


#This function reads all tasks from the CSV file and returns a list of TaskWithID objects.
def read_all_tasks() -> list[TaskWithID]:      
    with open(DATABASE_FILENAME, mode="r") as csvfile:      #Opens the CSV file in read mode.
        reader = csv.DictReader(csvfile)        #Creates a CSV reader object that reads each row as a dictionary.
        return [TaskWithID(**row) for row in reader]        #Converts each dictionary row into a TaskWithID object. ** unpacks the dictionary into keyword arguments. 
    
    
#This function reads a specific task from the CSV file based on its ID.
def read_task(task_id)-> TaskWithID | None:
    with open(DATABASE_FILENAME, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row["id"]) == task_id:
                return TaskWithID(**row)        #If matched, convert the row to a TaskWithID object and return it.
    return None  


#This function generates the next ID for a new task.
def get_next_id():
    try:
        with open(DATABASE_FILENAME,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            max_id = max(int(row["id"]) for row in reader)      #Finds the maximum ID in the CSV file.
            return max_id + 1
    except (FileNotFoundError, ValueError):     #If the file doesn't exist or is empty, start with ID 1.
        return 1

#This function writes a new task into the CSV file.
import os
def write_task_into_csv(task: Task):
    file_exists = os.path.isfile(DATABASE_FILENAME)      #Checks if the file already exists.
    with open(DATABASE_FILENAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=column_fields)
        if not file_exists:      #If the file doesn't exist, write the header.
            writer.writeheader()      #Writes the header (column names) to the CSV file.
        writer.writerow(task.model_dump())      # Writes the task data to the CSV file. model_dump() converts the Task object to a dictionary.
        
        

def create_tasks(task:Task)->TaskWithID:    # Creates a new task.
    new_id = get_next_id()
    task_with_id = TaskWithID(id=str(new_id),**task.model_dump())
    write_task_into_csv(task_with_id)
    return task_with_id
        
        

        
# def remove_task(task_id : int):
#     tasks = read_all_tasks()
#     with open(DATABASE_FILENAME,mode='w',newline="") as csvfile:
#         writer = csv.DictWriter(csvfile,fieldnames=column_fields)
        
        
