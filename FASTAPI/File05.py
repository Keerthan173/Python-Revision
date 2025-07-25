from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class User(BaseModel):      # Inherits BaseModel
    name: str
    age: int
    email: str

# Sending user data in request body
@app.post("/create_user")
async def create_user(user: User):
    return {
        "message": f"User {user.name} created",
        "age": user.age,
        "email": user.email
    }



# Why Pydantic?
# FastAPI uses Pydantic models to:
#     Validate input data (like JSON)
#     Ensure type safety


# Test in Swagger:
# Open: http://127.0.0.1:8000/docs
# Click POST /create_user and try this JSON input:
# {
#   "name": "Keerthan",
#   "age": 20,
#   "email": "keerthan@example.com"
# }
# Response:
# {
#   "message": "User Keerthan created",
#   "age": 20,
#   "email": "fekeerthan@example.comf"
# }
