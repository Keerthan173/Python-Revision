# if statement - block of code that will execute if its's condition is true
age=int(input("Age:"))  #()
if age>=60:
    if age==100:
        print("Centurian")
    print("Senior")
elif age>=18:
    print("Adult")
elif age>0:
    print("Child")
else:
    print("You are not born.....")
    



# Conditional Expression - ternary operator, a one-line shortcut for if-else.
x=-5
print("Positive" if x>0 else "Negative")  #Negative

num=int(input("Enter a number:"))
result="Even" if num%2==0 else "Odd"
print(result)

a,b=11,33
max=a if a>b else b
print(max)  #33