# Slicing - create a substring by extracting elements from another string
#                     indexing[] or slice()
#                      [start:stop:step]     
#                       stop - excluded

name= "Keerthan Mangaluru"
first_name=name[0:8]
print(first_name)  #Keerthan
last_name=name[9:]
print(last_name)  #Mangaluru

funky_name=name[::2] # → Step is positive
print(funky_name)  #Keta aglr
reversed_name=name[::-1] # → Step is negative
print(reversed_name)  #urulagnaM nahtreeK
# Positive step → start from left (default: index 0)
# Negative step → start from right (default: last index)


website1="http://google.com"
website2="http://wikipedia.com"
slicing=slice(7,-4)
print(website1[slicing])  #google
print(website2[slicing])  #wikipedia
#OR
print(website1[slice(7,-4)])  #google