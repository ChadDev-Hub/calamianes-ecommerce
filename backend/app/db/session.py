from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os
from .engine import DbEngine

async_session = async_sessionmaker(DbEngine.engine, expire_on_commit=False)




 
            

        

    

   
        
        
        
        