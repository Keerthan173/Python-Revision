# Type casting - convert the data type of a value to another data type
x=1
y=2.0
z="3"
print(x,y,z)            #1 2.0 3
print(int(y))           #2
# to make permanent change:
y=int(y)

print(z*3)          #333
print(int(z)*3)         #9

print((float)(x))          #1.0

# print("y:"+y)           #TypeError: can only concatenate str (not "int") to str
print("y:"+str(y))          #y:2
print("y:",y)           #y: 2