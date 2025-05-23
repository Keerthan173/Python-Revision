from typing import Union
from fastapi import FastAPI
from FASTAPI.routerExample import router
from FASTAPI.models import Book,BookResponse
app=FastAPI()        # Create an instance of the FastAPI class


@app.get("/")          # Define a route for the root URL
async def read_root():
    return {"Hello": "Keerthan"}

# uvicorn main:app --reload          # Run the server with this command


#Path paramter
@app.get("/items/{item_id}")
def path_func(item_id:int):
    return {"Item ID":item_id}

@app.get("/books/{book_id}")
async def read_book(book_id:int):
    return {
        "book_id":book_id,
        "title":"ABC Book",
        "author":"ABC Author"
    }
    

#Query paramter
@app.get("/query1/")
def query_func1(name : str ,roll: int):
    return {
        "Name":name,
        "Roll Number":roll
    }

@app.get("/query2/")
def query_func2(name : Union[str,None]=None ,roll: Union[int,None]=7):
    return {
        "Name":name,
        "Roll Number":roll
    }
    

    
@app.get("/books")
async def readBooks(year:int=None):
    if year:
        return {"Books":[{"Title":"Book1","Year":year},{"Title":"Book2","Year":year}]}
    return {"Books":"All Books"}

# app.include_router(router,)

@app.post("/book")
async def create_book(book:Book):
    return {
        "Message":"Book Created",
        "Book":book
    }
    
@app.get("/allbooks", response_model=list[BookResponse])
async def read_all_books():
    return [
        {"id":1,"title": "Book1", "author": "Author1"},
        {"id":2,"title": "Book2", "author": "Author2"}
    ]
