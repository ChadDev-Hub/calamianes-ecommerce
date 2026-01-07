from fastapi import APIRouter, Depends
from ..dependencies.security import get_current_user
from sqlalchemy import select

router = APIRouter(prefix="/shop", tags=["Shops"])
current_user_depends = Depends(get_current_user)

@router.post("/create")
async def create_shop(get_user:dict = current_user_depends):
    username = get_user.get("username")
    return username
