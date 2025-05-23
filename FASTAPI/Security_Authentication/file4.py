# Protect a Route
# • Create a protected route like /me
# • Use Depends() with a get_current_user() function
# • This function should:
# o Read the token from the header
# o Decode it
# o Return user info
# • If token is missing or invalid, return 401

from datetime import datetime, timedelta, timezone
import bcrypt
from fastapi import Depends, FastAPI, HTTPException
import jwt
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"

dummy_user = {
    "email": "user@example.com",
    "hashed_password": bcrypt.hashpw("password123".encode('utf-8'), bcrypt.gensalt())
}

class LoginRequest(BaseModel):
    email: str
    password: str
    
# Function to create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post("/login")
def login(login_request: LoginRequest):
    email = login_request.email
    password = login_request.password
    
    if email != dummy_user["email"]:
        raise HTTPException(status_code=401, detail="Invalid email")
    
    if not bcrypt.checkpw(password.encode('utf-8'), dummy_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    access_token = create_access_token({'email':email})
    return {"access_token":access_token}

@app.get('/me')
def read_current_user(current_user: dict = Depends(get_current_user)):
    return {
        "message":"You are authenticated",
        "user": current_user
    }