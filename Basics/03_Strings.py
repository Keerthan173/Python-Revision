name="Bro Code"
print(len(name))            #8
print(name.find("B"))           #0
print(name.find("b"))           #-1
print(name.upper())         #BRO CODE
print(name.split(" "))          #['Bro', 'Code']
print(name.count("o"))          #2
print(name.replace("o","abc"))          #Brabc Cabcde
print(name.isalnum())           #False    (Space is present)
print(name.isdigit())           #False


y="BroCode"
print(y.isalnum())          #True

x="123"
print(x.isdigit())          #True



# Validate user input exercise:
#     1. username is not more than 12 characters.
#     2. username must not contain space and digits.
username=input("Enter Username:")
if len(username)>12:
    print("Username can't be more than 12 chracters.")
elif not username.find(" "):            #If not found it will return -1
    print("Username can't have space.")
elif not username.isalpha():                #Return True if the string is an alphabetic string, False otherwise.
    print("Username cannot have digits.")
else:
    print(f"Welcome {username}!")
# Output:
# Enter Username:Bro Code
# Username cannot have digits.

# Enter Username:BroCode
# Welcome BroCode!