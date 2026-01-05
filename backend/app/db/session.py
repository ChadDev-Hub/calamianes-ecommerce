from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
from .base import Base
import os

class DbSession:
    '''DB SESSION FOR POSTGRESQL CONNECTION'''
    def __init__(self) -> None:
        load_dotenv()
        USERNAME = os.getenv("USERNAME")
        PASSWORD = os.getenv("PASSWORD")
        DBNAME = os.getenv("DBNAME")
        HOST = os.getenv("HOST")
        PORT = os.getenv("PORT")
        self.engine = create_async_engine(f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}")
        
    async def create_table(self):
        '''
        Funtion that Create table for Base metadata
        '''
        print(Base.metadata.tables.keys())
        print("...CREATING TABLE...")
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("...TABLE CREATED...")
    async def close(self):
        """Close Engine Connection
        """
        if self.engine:
            await self.engine.dispose()
            
        
        
        
        