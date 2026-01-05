from app.db.session import DbSession
import asyncio
from app.models.user import User
from app.models.shop import Shop
from app.models.product import Product
from app.models.product_image import ProductImage 

async def c_engine():
    session = DbSession()
    await session.create_table()

if __name__ == "__main__":
    asyncio.run(c_engine())
