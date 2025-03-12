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