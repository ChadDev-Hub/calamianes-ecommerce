from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, HTTPException, status, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio.session import AsyncSession
from ..utils.authentication import authenticate_user
from ..dependencies.session import get_session
from ..utils.access_token import create_access_token, create_refresh_token
from ..schema.token import Token

router = APIRouter(prefix="/auth", tags=["Auth"])


session_depends = Depends(get_session)

@router.post("/token")
async def log_for_access_token(response:Response, form_data:OAuth2PasswordRequestForm = Depends(), session:AsyncSession = session_depends):
    user = await authenticate_user(session=session, password=form_data.password, user_name=form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorect Username or Password")
    data = {
        "sub": user.user_name,
        "id": user.id
    }
    access_token = create_access_token(data=data)
    refresh_token = create_refresh_token(data=data)
    response.set_cookie(key="refresh_token", value=refresh_token, expires=datetime.now(timezone.utc) + timedelta(days=7))
    return Token(access_token=access_token, token_type="bearer")
