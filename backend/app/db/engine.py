import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from .base import Base

load_dotenv()
USERNAME = os.getenv("POSTGRESUSER")
PASSWORD = os.getenv("PASSWORD")
DBNAME = os.getenv("DBNAME")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


class DbEngine:
    engine = create_async_engine(f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}")

    @classmethod
    async def create_table(cls):
            '''
            Funtion that Create table for Base metadata
            '''
            print(Base.metadata.tables.keys())
            print("...CREATING TABLE...")
            async with cls.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("...TABLE CREATED...")

    @classmethod
    async def close(cls):
            """Close Engine Connection
            """
            if cls.engine:
                await cls.engine.dispose()