# index operator [] = gives access to a sequence's element(str, list, tuple)

name = "bro Code!"

if(name[0].islower()):
    name = name.capitalize()
print(name) # Bro code!


first_name = name[0:3]
# first_name = name[:3]
print(first_name.upper()) # BRO


last_name = name[4:-1]
print(last_name) # code

last_char = name[-1]
print(last_char) #!