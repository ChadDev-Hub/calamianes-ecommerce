from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/")
async def signup():
    return({
        "Greetings": "Hellow World"
    })