from sqlalchemy.ext.asyncio.session import AsyncSession
from .hashing import verify_password
from sqlalchemy import select
from ..models import User

async def authenticate_user(session:AsyncSession, password:str, user_name:str):
    user = await session.scalar(select(User).where(User.user_name == user_name))
    if not user:
        return False
    if not verify_password(password,  user.password):
        return False
    return user