# *args = parameter that will pack all arguments into a tuple.
#         useful so that a function can accept a varying amount of arguments.

def add1(num1, num2):
    return num1 + num2

print(add1(3,4)) # 7
# print(add1(1,2,3)) # TypeError: add1() takes 2 positional arguments but 3 were given


def add2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add2(1,2)) # 3
print(add2(1,2,3)) # 6
print(add2()) # 0



def func(*args):
    return args[0]
print(func(1,2,3)) # 1
print(func(1)) # 1
# print(func()) # IndexError: tuple index out of range



def myFunc(*args):
    args[0] = 3 # TypeError: 'tuple' object does not support item assignment (Tuple is immutable)
    print("Hello")
# myFunc(1,2,3)


def myFunc(*args):
    args = list(args)
    args[0] = 3 # (List is mutable)
    print("Hello")
myFunc(1,2,3) # Hello