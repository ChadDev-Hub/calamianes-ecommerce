from datetime import timedelta
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio.session import AsyncSession
from ..utils.authentication import authenticate_user
from ..dependencies.session import get_session
from ..utils.access_token import create_access_token
from ..schema.token import Token

router = APIRouter(prefix="/auth", tags=["Auth"])
ACCESS_TOKEN_EXPIRE = 15

session_depends = Depends(get_session)

@router.post("/token")
async def log_for_access_token(form_data:OAuth2PasswordRequestForm = Depends(), session:AsyncSession = session_depends):
    user = await authenticate_user(session=session, password=form_data.password, user_name=form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorect Username or Password")
    data = {
        "sub": user.user_name,
        "id": user.id
    }
    access_token = create_access_token(data=data, expire_delta=timedelta(seconds=ACCESS_TOKEN_EXPIRE))
    return Token(access_token=access_token, token_type="bearer")
