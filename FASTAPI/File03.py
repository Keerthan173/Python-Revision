from fastapi import FastAPI

app = FastAPI()

# Query parameter: name (optional), age (required)
@app.get("/greet")
async def greet_user(age: int, name: str = "Guest"):
    return {"message": f"Hello, {name}! You are {age} years old."}


# http://127.0.0.1:8000/greet?age=20&name=Keerthan
# {
#   "message": "Hello, Keerthan! You are 20 years old."
# }

# (without name): http://127.0.0.1:8000/greet?age=20
# {
#   "message": "Hello, Guest! You are 20 years old."
# }


# Query Parameters → Filter or modify the result
# Used to add optional data like filters, sort order, search, etc.