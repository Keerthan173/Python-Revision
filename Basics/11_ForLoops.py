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
    time.sleep(1)       # Delay execution for a given number of seconds. 
print("HAPPY NEW YEAR!")