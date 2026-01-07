from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
import jwt

load_dotenv()
SECRETE_KEY = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")
def create_access_token(data:dict, expire_delta:timedelta | None = None):
    to_encode = data.copy()
    if expire_delta:
        expire  = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({
        "exp": expire
    })
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRETE_KEY, algorithm=ALGORITHM)
    return encoded_jwt

