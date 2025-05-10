# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1)+fibonacci(n-2)

# i=int(input("Enter a number:"))
# if(i<0):
#     print("Number should be positive.")
# else:
#     print(fibonacci(i))


# Write a function that takes two numbers and a function as arguments,then applies the function to the numbers.
def operate(x,y,func):
    return func(x,y)

def multiply(a,b):
    return a*b

print(operate(3,4,multiply))