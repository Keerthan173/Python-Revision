name=""
while len(name)==0:
    name=input("Enter your name:")
print("Hello "+name)
#OR
name=None
while not name:
    name=input("Enter your name:")
print("Hello "+name)

# Output:
# Enter your name:
# Enter your name:
# Enter your name:Keerthan K
# Hello Keerthan K



# Compound interest calculator
# Final amount,A= P(1 + r/100)^t
principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter the principle amount:"))
    if(principle<=0):
        print("Principle amount cannot be zero or less.")

while True:
    rate=float(input("Enter the interest rate:"))
    if(rate<0):
        print("Interest Rate cannot be negative.")
    else:
        break
        
while True:
    time=float(input("Enter the time(in years):"))
    if(time<=0):
        print("Time cannot be negative.")
    else:
        break
        
print(f"Principle:{principle} Rate:{rate} Time:{time}")
total=principle * pow((1+rate/100),time)
print(f"Total:{total:.2f}")
# Output:
# Enter the principle amount:-57
# Principle amount cannot be zero or less.
# Enter the principle amount:0
# Principle amount cannot be zero or less.
# Enter the principle amount:100
# Enter the interest rate:3
# Enter the time(in years):2
# Principle:100.0 Rate:3.0 Time:2.0
# Total:106.09
