temp=int(input("Temperature:"))
if temp>=0 and temp<=10 :
    print("Cold")
elif temp>=10 and temp<=40 :
    print("Temperature is normal.")
    print("Go outside.")
elif temp<0 or temp>50 :
    print("Not normal.....")
    
    
# Output:
# Temperature:5  
# Cold

# Temperature:35
# Temperature is normal.
# Go outside.

# Temperature:-23
# Not normal.....


x=False
if not x:                  #OR   if not(x)
    print("Hello")
# Output:
# Hello