# Exercise 3: FastAPI Login Route
# • Create a /login route in FastAPI:
# o Accepts email and password
# o Verifies against a dummy user stored in code
# o Returns a JWT token if login is correct

from fastapi import FastAPI, HTTPException
import jwt
from pydantic import BaseModel
import bcrypt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "keerthan_secret"
ALGORITHM = 'HS256'

app = FastAPI()

dummy_user = {
    "email": "user@gmail.com",
    "hashed_password": bcrypt.hashpw( "password123".encode('utf-8'), bcrypt.gensalt())
}

class Login(BaseModel):
    email: str
    password: str
    
def create_access_token(data:dict,expires_delta:timedelta=timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode, SECRET_KEY , algorithm=ALGORITHM)
    return token
    
@app.post("/login")
def login(login_request: Login):
    email = login_request.email
    password = login_request.password
    
    if email != dummy_user["email"]:
        raise HTTPException(status_code=401, detail="Invalid email")
    
    if not bcrypt.checkpw(password.encode('utf-8'), dummy_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    access_token = create_access_token({'email':email})
    return {"access_token":access_token}