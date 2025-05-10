from fastapi import FastAPI
from routerExample import router
from models import Book,BookResponse
app=FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id:int):
    return {
        "book_id":book_id,
        "title":"ABC Book",
        "author":"ABC Author"
    }
    

@app.get("/author/{author_id}")
async def author_info(author_id:int):
    return {
        "author_id":author_id,
        "author_name":"ABC"
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
