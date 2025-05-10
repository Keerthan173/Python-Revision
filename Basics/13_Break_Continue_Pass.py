# break - used to terminate the loop entirely.
while True:
    name=input("Enter your name:")
    if name!="":
        break
    print("Retry")
print("Hello",name)
# Output:
# Enter your name:
# Retry
# Enter your name:Bro
# Hello Bro


# continue - skips the current and executes next iteration.
phone="123-456-789"
for i in phone:
    if i=="-":
        continue
    print(i,end="")
# Output:
# 123456789


# pass - does nothing, acts like a placeholder.
for i in range(1,11):
    if i==5:
        pass
    else:
        print(i,end=" ")
# Output:
# 1 2 3 4 6 7 8 9 10
