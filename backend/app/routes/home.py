from fastapi import APIRouter


router = APIRouter(tags=["homepage"])

@router.get("/")
async def homepage():
    return {
        "title" : "Calamianes Ecommerce Website",
        "description" : "Calamianes Ecommerce Website is a modern online marketplace designed to connect local sellers and consumers in the Calamianes region. The platform provides a secure, user-friendly shopping experience with seamless product browsing, reliable transactions, and efficient order management."
    }   