from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey, VARCHAR
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.product import Product

# ---------------------------------------SHOP-----------------------------------------------
class Shop(Base):
    __tablename__ = "shops"
    id:Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"), type_=Integer)
    shop_name:Mapped[str] = mapped_column(type_=Text)
    description:Mapped[str] = mapped_column(type_=VARCHAR(200))
    user: Mapped["User"] = relationship("User", back_populates="shop")
    prod: Mapped[List["Product"]] = relationship("Product",back_populates="shop", cascade="all, delete-orphan")