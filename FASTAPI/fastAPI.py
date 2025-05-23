from fastapi import FastAPI
import FASTAPI.routerExample as routerExample
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/calculate")
def add_number(number1: int, number2: int):
    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    division = number1 / number2 if number2 != 0 else "undefined"
    return {
        "sum": f"{number1} + {number2} = {sum_result}",
        "difference": f"{number1} - {number2} = {difference}",
        "product": f"{number1} * {number2} = {product}",
        "division": f"{number1} / {number2} = {division}"
    }
    
# @app.get("/items/{item}")
# def myfunc(item:str):
#     return{
#         "message":f"{item} is receeived"
#     }


app.include_router(routerExample.router)