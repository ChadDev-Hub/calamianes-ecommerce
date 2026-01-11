from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey, VARCHAR, Boolean
from pydantic import BaseModel
from typing import List, TYPE_CHECKING
from ..db.base import Base

if TYPE_CHECKING:
    from .business import Business
# ---------------------------------------USER-----------------------------------------------
class User(Base):
    __tablename__ = "user_account"
    id:Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    user_name:Mapped[str] = mapped_column(type_=Text, unique=True)
    first_name:Mapped[str] = mapped_column(type_=Text)
    last_name:Mapped[str] = mapped_column(type_=Text)
    email:Mapped[str] = mapped_column(type_=Text)
    password: Mapped[str] = mapped_column(type_=Text)
    is_active: Mapped[bool] = mapped_column(type_=Boolean, default=True)
    isadmin: Mapped[bool] = mapped_column(type_=Boolean, default=False) 

    shop: Mapped[List["Business"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    
    


    
