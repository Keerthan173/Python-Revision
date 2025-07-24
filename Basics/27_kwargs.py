# **kwargs == parameter that will pack all arguments into a dictionary.
#             works like *args but for keyword arguments.

def hello(first,last):
    print("Hello", first, last)
    
hello(first="Bro", last="Code") # Hello Bro Code
hello("Bro", "Code") # Hello Bro Code
# hello(first="Bro", middle="Dude", last="Code") # TypeError: hello() got an unexpected keyword argument 'middle'



def hello2(**kwargs):
    print("Hello", kwargs["first"], kwargs["last"])
    
hello2(first="Bro", last="Code") # Hello Bro Code
hello2(first="Bro", middle="Dude", last="Code") # Hello Bro Code Dude



def hello3(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
    print()
        
hello3(first="Bro", last="Code") # Hello Bro Code
hello3(first="Bro", middle="Dude", last="Code") # Hello Bro Dude Code
hello3(title="Mr.", first="Bro", middle="Dude", last="Code") # Hello Mr. Bro Dude Code