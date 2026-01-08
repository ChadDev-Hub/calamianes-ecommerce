from app.db.engine import DbEngine
import asyncio
from app import models

async def c_engine():
    session = DbEngine()
    await session.create_table()

if __name__ == "__main__":
    asyncio.run(c_engine())
