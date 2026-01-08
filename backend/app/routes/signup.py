from fastapi import APIRouter, Depends, Form
from ..dependencies.session import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from ..models import User
from sqlalchemy import select
from ..schema.signupform import SignUpForm
from fastapi.exceptions import HTTPException
import jwt
from jwt.exceptions import InvalidTokenError
from dotenv import load_dotenv
from ..utils.hashing import get_password_hash
import os

load_dotenv()
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
async def signup(data:SignUpForm = Form(), session:AsyncSession = Depends(get_session)):
    query = select(User).where(User.email == data.email)
    existing_user  = await session.execute(query)
    if existing_user.scalars().all():
        raise HTTPException(409, "Email Already Exists")
    new_user = User(
        user_name = data.username,
        first_name = data.firstname,
        last_name = data.lastname,
        email= data.email,
        password =  get_password_hash(password=data.password),
        isadmin = False
    )
    
    session.add(new_user)
    await session.commit()
    await session.close()
    return {
        "status": "Signup Sucessful"
    }