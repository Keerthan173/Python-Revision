from fastapi import FastAPI
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
    
    
# Go to: http://127.0.0.1:8000 → returns {"message": "Hello World"}

# Try this (with query params):
# http://127.0.0.1:8000/calculate?number1=10&number2=5
# Output:
# {
#   "sum": "10 + 5 = 15",
#   "difference": "10 - 5 = 5",
#   "product": "10 * 5 = 50",
#   "division": "10 / 5 = 2.0"
# }