# str.format() = more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item) # The cow jumped over the moon
print("The {} jumped over the {}".format(animal, item)) # The cow jumped over the moon
print("The {0} jumped over the {1}".format(animal, item)) # The cow jumped over the moon
print("The {1} jumped over the {0}".format(animal, item)) # The moon jumped over the cow


text = "The {} jumped over the {}"
print(text.format(animal, item)) # The cow jumped over the moon"



# We can use keyword arguments in the format method as well:
print("The value of {x} is {y}".format(x=5, y=10)) # The value of 5 is 10
print("The value of {y} is {x}".format(x=5, y=10)) # The value of 10 is 5