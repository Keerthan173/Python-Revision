from fastapi import FastAPI
from database import create_db_and_tables, engine
from sqlmodel import Session

from models import User
app=FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
#Create a new user
@app.post("/users/")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

#Get user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return {"error": "User not found"}
        return user

#Update user email
@app.put("/users/{user_id}")
def update_user(user_id: int, email: str):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return {"error": "User not found"}
        user.email = email
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

#Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return {"error": "User not found"}
        session.delete(user)
        session.commit()
    return {"message": "User deleted successfully"}
