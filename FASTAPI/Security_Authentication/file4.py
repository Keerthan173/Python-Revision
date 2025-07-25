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
from fastapi import Depends, FastAPI, HTTPException, Header
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

# Login route: returns access token
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


# ✅ Dependency to get current user from token
def get_current_user(authorization: str = Header(...)):
    #FastAPI automatically reads the Authorization header from the request.
    # Example header:
        # Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...
    try:
        scheme, _, token = authorization.partition(" ")
        # Splits the header into:
        # scheme = "Bearer"
        # token = "eyJhbGciOi..." (your JWT)
        # partition(" ") splits once at the first space.
        
        if scheme.lower() != "bearer":          # Makes sure the scheme is Bearer
            raise HTTPException(status_code=401, detail="Invalid auth scheme")
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        return {
            "email":email
        }
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    
# 🔐 Protected Route
@app.get("/me")
def read_current_user(current_user: dict = Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user": current_user
    }

# 🔹 Depends(get_current_user)
# Tells FastAPI:
# 👉 "Before calling read_current_user(), run get_current_user()."

# The result of get_current_user() (a dictionary with user info) is injected into the current_user parameter.