from sqlalchemy.ext.asyncio.session import AsyncSession
from ..db.session import async_session
from fastapi import Depends
from contextlib import asynccontextmanager

#  SQL ALCHEMY GET SESSION FUNCTION

async def get_session():
    """
    This get the session and yields the operation until close 
    """
    async with async_session() as session:
        yield session
