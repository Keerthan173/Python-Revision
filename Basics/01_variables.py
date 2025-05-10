# Variable - a container for a value.

name="Keerthan"
print(name)         #Keerthan
print("Hello "+name)            #Hello Keerthan
print(type(name))           #<class 'str'>
print(name*2)           #KeerthanKeerthan


first_name="Bro"
last_name="Code"
full_name=first_name+" "+last_name
print(full_name)            #Bro Code


age=20
print(type(age))            #<class 'int'>
age+=1
print(age)          #21
# print("My age is:"+age)         #TypeError: can only concatenate str (not "int") to str
print("My age is:",age)         #My age is: 21
print("My age is :"+str(age))           #My age is :21


height=250.5
print(type(height))         #<class 'float'>
print("My height is:" +str(height)+ "cm")           #My height is:250.5cm


human=False
print(type(human))          #<class 'bool'>
print("Are you a human? "+str(human))           #Are you a human? False
