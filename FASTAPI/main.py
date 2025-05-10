from fastapi import FastAPI
app = FastAPI()        # Create an instance of the FastAPI class

@app.get("/")          # Define a route for the root URL
def read_root():
    return {"Hello": "Keerthan"}

# uvicorn main:app --reload          # Run the server with this command
