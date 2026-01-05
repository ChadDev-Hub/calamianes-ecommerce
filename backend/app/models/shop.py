from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey, VARCHAR
from ..db.base import Base
from geoalchemy2 import Geometry


if TYPE_CHECKING:
    from .user import User
    from .product import Product

# ---------------------------------------SHOP-----------------------------------------------
class Shop(Base):
    __tablename__ = "shops"
    id:Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    user_id:Mapped[int] = mapped_column(ForeignKey("user_account.id"), type_=Integer)
    shop_name:Mapped[str] = mapped_column(type_=Text)
    description:Mapped[str] = mapped_column(type_=VARCHAR(200))
    geom: Mapped[str] = mapped_column(type_=Geometry(geometry_type="POINT", srid=4326))
    
    # RELATIONSHIPS
    user: Mapped["User"] = relationship("User", back_populates="shop")
    prod: Mapped[List["Product"]] = relationship("Product",back_populates="shop", cascade="all, delete-orphan")