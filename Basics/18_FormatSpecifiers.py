# format specifiers are used to control the output format of values. 

price=3.14159
print(f"Price 1 is {price:.2f} dollars")  #Price 1 is 3.14 dollars
print(f"Price 1 is {price:10} dollars")  #Price 1 is    3.14159 dollars
print(f"Price 1 is {price:010} dollars")  #Price 1 is 0003.14159 dollars
print(f"Price 1 is {price:<10} dollars")  #Price 1 is 3.14159    dollars
print(f"Price 1 is {price:>10} dollars")  #Price 1 is    3.14159 dollars