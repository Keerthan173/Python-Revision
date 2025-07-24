# Exception = events detected during execution that disrupt the normal flow of a program.

# x = int(input("Numerator:"))
# y = int(input("Denominator:"))
# res = x/y
# print(res)

# Output:
# Numerator:5
# Denominator:0
# ZeroDivisionError: division by zero


# To handle exceptions, we can use try and except blocks.
try:
    x = int(input("Numerator:"))
    y = int(input("Denominator:"))
    res = x/y
    print(res)
except ZeroDivisionError as e:
    print("Division by zero is not allowed.", e)
except ValueError as e:
    print("Invalid input, please enter a number.", e)
except Exception as e:
    print("Something went wrong :(", e)
else:
    print("Division successful:", res)
finally:
    print("Closing resources...")

print("Program continues...")

# Output:
# Numerator:5
# Denominator:0
# Division by zero is not allowed. division by zero
# Closing resources...
# Program continues...

# Numerator:5
# Denominator:pizza
# Invalid input, please enter a number. invalid literal for int() with base 10: 'pizza'
# Closing resources...
# Program continues...

# Numerator:5
# Denominator:3
# 1.6666666666666667
# Division successful: 1.6666666666666667
# Closing resources...
# Program continues...