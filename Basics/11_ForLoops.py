# Execute a block of code for fixed number of times. 

for i in range(5):
    print(i)
#Output:
# 0
# 1
# 2
# 3
# 4

for i in range(5,15,2):
    print(i)
#Output:
# 5
# 7
# 9
# 11
# 13

for i in range(5,2,-1):
    print(i)
#Output:
# 5
# 4
# 3

name="Kee"
for i in name:
    print(i)
#Output:
# K
# e
# e


import time
for count in range(10,0,-1):
    print(count)
    time.sleep(1)
print("HAPPY NEW YEAR!")


#Count-down timer
timeSec=int(input("Enter time in seconds:"))
for x in range(0,timeSec):
    