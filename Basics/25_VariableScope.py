# Scope = The region that a variable is recognized.

first_name = "Bro"           # Global variable
def display_name():
    last_name = "Code"       # Local variable - available from inside the region it is created
    print(last_name)
    
print(first_name)
# print(last_name) # NameError: name 'last_name' is not defined