from fastapi import FastAPI  # Importing FastAPI class from the fastapi module

app = FastAPI()  # Creating an instance of the FastAPI app

# This route handles GET requests to the root URL "/"
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}  # Returns a JSON response

# Run the server
# uvicorn main:app --reload
    # Open: http://127.0.0.1:8000
    # Swagger UI: http://127.0.0.1:8000/docs