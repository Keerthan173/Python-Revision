# FastAPI - Security and Authentication Exercises

# Exercise 1: Password Hashing & Verification
# • Create a simple script:
# o Input a password
# o Hash it with bcrypt
# o Store it in a variable or dictionary
# o Prompt the user again to enter the password
# o Verify it using the hash
# • Try hashing the same password multiple times—observe the hashes
# • Print “Access granted” or “Invalid password” based on verification

import bcrypt

password = input("Enter a password:").encode('utf-8')     # Encode the password to bytes
# bcrypt requires the password to be in bytes, so we encode it using utf-8.

salt = bcrypt.gensalt(12)       # Generate a salt with 12 rounds.
# Rounds are the number of iterations the hashing algorithm will run.
# The higher the number of rounds, the more secure the hash will be, but it will also take longer to compute.

hashed_password = bcrypt.hashpw(password, salt)     # Hash the password with the salt

user = {"userName": "user1", "password": hashed_password}       # Store the hashed password in a dictionary

attempt = input("Re-enter the password to verify:").encode('utf-8')     # Prompt the user to enter the password again and encode it to bytes

if bcrypt.checkpw(attempt , user["password"]):      # Check if the entered password matches the hashed password
    print("Access granted")
else:
    print("Invalid password")
    
    
    
# Show how hashing the same password gives different results
print("\n🔁 Hashing the same password 3 times:")
for i in range(3):
    new_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    print(f"Hash {i+1}: {new_hash.decode()}")