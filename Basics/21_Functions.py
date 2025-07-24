# Functions = a block of code which is executed only when it is called

def hello():
    print("Hello World!")
    
hello() # Hello World!



def helloName(name):
    print("Hello", name)
     
my_name = "Bro"
helloName(my_name) # Hello Bro
helloName("Dude") # Hello Dude

# hello("Keerthan") # TypeError: hello() takes 0 positional arguments but 1 was given
helloName("Keerthan") # Hello Keerthan



def display(name, age):
    print("Name:", name)
    print("Age:",age)

display("Keerthan K", 20)
# Name: Keerthan K
# Age: 20
