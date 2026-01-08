from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
import jwt
ACCESS_TOKEN_EXPIRE = 30
REFRESH_TOKEN_EXPIRE = 7
load_dotenv()
SECRETE_KEY = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")
def create_access_token(data:dict):
    to_encode = data.copy()
    expire  = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    to_encode.update({
        "exp": expire,
        "type": "access_token"
        })
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRETE_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data:dict):
    to_encode = data.copy()
    expire  = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE)
    to_encode.update({
        "exp" : expire,
        "type": "refresh_token"
    })
    acces_token = jwt.encode(payload=to_encode, key=SECRETE_KEY, algorithm=ALGORITHM)
    return acces_token