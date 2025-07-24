pi=3.14
print(round(pi))  #3
print(pow(pi,2))  #9.8596
print(abs(pi))  #3.14
print(abs(-2))  #2
print(abs(0))  #0

import math
print(math.ceil(pi))  #4
print(math.floor(pi))  #3
print(math.factorial(5))  #120
print(math.factorial(int(pi)))  #6
print(math.sqrt(pi))  #1.772004514666935

x,y,z=1,2,3
print(max(x,y,z))  #3
print(min(x,y,z))  #1

# max(), min(), len(), sum(), etc. are built-in functions in Python, so you don’t need to use math. with them.
# math.ceil(), math.floor(), and math.sqrt() are part of the math module, so you must prefix them with math.
