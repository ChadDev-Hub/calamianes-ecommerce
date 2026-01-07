from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from ..models import User
from ..dependencies.session import get_session
import jwt
from dotenv import load_dotenv
import os
from jwt.exceptions import InvalidTokenError

load_dotenv()
SECRET_KEY = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")
outh2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
session_depends = Depends(get_session)

async def get_current_user(token:str = Depends(outh2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate" : 'Bearer'}
    )
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)
        user_name = payload.get("sub")
        user_id = payload.get("id")
        if not user_name:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    return {
        "username": user_name,
        "id": user_id
    }
        

