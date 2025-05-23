from typing import Annotated
from fastapi import FastAPI, Depends, status , HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_user_db = {
    "user1":{
        "username": "user1",
        "email": "ex1@gmail.com",
        "password": "password1",
        "disabled": False
    },
    "user2":{
        "username": "user2",
        "email": "ex2@gmail.com",
        "password":"password2",
        "disabled":True
    }
}

app = FastAPI()

def fake_hash(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None
    
class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode(token):
    user = get_user(fake_user_db,token)
    return user

async def get_