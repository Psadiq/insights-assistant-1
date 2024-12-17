from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy function to simulate current user (API security)
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token == "fake-token":
        return "fake-user"
    else:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    # app/security.py

def authenticate_request(api_key: str) -> bool:
    # Your authentication logic here
    if api_key == "valid_api_key":  # Replace with actual validation logic
        return True
    return False
