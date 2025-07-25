from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def user_root():
    return {
        "message": "Hello User!",
    }

# Path parameter: user_id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "message": f"User with ID {user_id} was requested"
        }

# http://127.0.0.1:8000/users/101
# {
#   "message": "User with ID 101 was requested"
# }


# Path Parameters → Identify a specific resource
# Used when you want to access a specific item or resource.