# Exercise 2: Token Creation & Decoding
# • Write a function to create a JWT access token using python-jose
# • Create another function to decode and read the token
# • Try using different payloads (e.g. name, email, id)
# • Experiment with expiration time and see what happens when it's expired

from jose import jwt , JWTError
from datetime import datetime, timedelta , timezone

# Define a secret key and algorithm for JWT
SECRET_KEY = "my_secret_key"    #secret string only your app knows — it’s used to sign and verify tokens.
ALGORITHM = "HS256"     #ALGORITHM is the method to encode the token (HS256 is a common choice).

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create a JWT access token with an expiration time.
    :param data: The payload data to include in the token.
    :param expires_delta: Optional expiration time delta.
    :return: The encoded JWT token as a string.
    """
    to_encode = data.copy()     # Copy the data to avoid modifying the original
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta     # Set the expiration time
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)     # Default expiration time is 15 minutes
        
    to_encode.update({"exp": expire})     # Add the expiration time to the payload
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)     # Encode the payload with the secret key and algorithm
    return encoded_jwt     # Return the encoded JWT token

def decode_access_token(token: str):
    """
    Decode a JWT access token and return the payload data.
    :param token: The JWT token to decode.
    :return: The decoded payload data.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])     # Decode the token using the secret key and algorithm
        return payload     # Return the decoded payload
    except JWTError as e:
        print(f"Token decoding error: {e}")     # Handle any decoding errors
        return None
    
# Example usage
if __name__ == "__main__":
    # Create a token with a payload
    payload = {"name": "Keerthan K", "email": "keerthan@example.com", "id": 123}
    token = create_access_token(data=payload, expires_delta=timedelta(minutes=1))     # Create a token with a 5-minute expiration time
    print(f"Generated Token: {token}")     # Print the generated token
    
    # Decode the token
    decoded_payload = decode_access_token(token)     # Decode the token
    if decoded_payload:
        print(f"Decoded Payload: {decoded_payload}")     # Print the decoded payload
    else:
        print("Failed to decode token")     # Handle decoding failure
        
    # Wait for the token to expire (for testing purposes)
    # import time
    # time.sleep(70)     # Sleep for 5 minutes to let the token expire
    # expired_payload = decode_access_token(token)     # Attempt to decode the expired token
    # if expired_payload:
    #     print(f"Decoded Payload: {expired_payload}")     # Print the decoded payload
    # else:
    #     print("Token has expired")     # Handle token expiration
    
