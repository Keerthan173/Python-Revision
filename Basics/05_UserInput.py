name=input("What is your name?") #(Bro)
print("Hello "+name)            #Hello Bro


age=input("Enter your age:")  #(Enter your age:20)
print(age)          #20
print(type(age))            #<class 'str'>
# age=age+1           #TypeError: can only concatenate str (not "int") to str


x=int(input("Value:"))  #(Value:77)
print(type(x))          #<class 'int'>
print(x+1)          #78


myAge=int(input("What's your age?"))  #(What's your age?16)
myAge+=1
print(myAge)            #17
# print("Your age is "+myAge)         #TypeError: can only concatenate str (not "int") to str
print("Your age is "+str(myAge)+" years old.")          #Your age is 17 years old.
print("Your age is",myAge,"years old.")         #Your age is 17 years old.


height=float(input("How tall are you?"))  #(How tall are you?32.3)
print(type(height))         #<class 'float'>
print(height+1)         #33.3
