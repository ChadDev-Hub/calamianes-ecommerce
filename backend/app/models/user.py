from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey, VARCHAR
from pydantic import BaseModel
from typing import List, TYPE_CHECKING
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.shop import Shop
# ---------------------------------------USER-----------------------------------------------
class User(Base):
    __tablename__ = "user_acount"
    id:Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    user_name:Mapped[str] = mapped_column(type_=Text, unique=True)
    email:Mapped[str] = mapped_column(type_=Text)
    shop: Mapped[List["Shop"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    


    
