# Positional arguments: Order matters.
def hello(first, last):
    print(first, last)
hello("Bro","Code") # Bro Code
hello("Code","Bro") # Code Bro


# Keyword arguments: Order of the arguments doesn't matter.
# But we should pass an identifiers with the arguments.
hello(last="Code", first="Bro") # Bro Code
hello(first="Bro", last="Code") # Bro Code
hello(last="K", first="Keerthan") # Keerthan K
