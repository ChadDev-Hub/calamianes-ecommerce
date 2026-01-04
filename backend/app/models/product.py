from __future__ import annotations
from typing import List, TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Text, VARCHAR
from geoalchemy2 import Geometry

if TYPE_CHECKING:
    from app.models.shop import Shop
    from app.models.product_image import ProductImage
# -------------------------------------Product----------------------------------------------
class Product(Base):
    __tablename__ = "product"
    id:Mapped[int] = mapped_column("id", primary_key=True, type_=Integer)
    shop_id:Mapped[int] = mapped_column(ForeignKey("shops.id"), type_=Integer)
    product_name:Mapped[str] = mapped_column(type_=Text)
    description:Mapped[str] = mapped_column(type_=VARCHAR(200))
    geom:Mapped[str] = mapped_column(type_=Geometry("POINT", 4326))
    shop:Mapped["Shop"] = relationship(back_populates="prod")
    prod_image: Mapped[List['ProductImage']] = relationship(back_populates="prod", cascade="all, delete-orphan")