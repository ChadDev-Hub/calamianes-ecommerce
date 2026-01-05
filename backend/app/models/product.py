from __future__ import annotations
from typing import List, TYPE_CHECKING
from ..db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Text, VARCHAR
from geoalchemy2 import Geometry

if TYPE_CHECKING:
    from .shop import Shop
    from .product_image import ProductImage
# -------------------------------------Product----------------------------------------------
class Product(Base):
    '''
    Represents Product table
    #### Columns:
        - id: The Primary key of this table
        - shop_id: Foreign key relation to shop
        - product_name: The Name of The Product
        - description: The Product Description the shows unique about the Product
    #### RELATIONSHIP:
        - shop: Shops where this Product is sold
        - prod_image: List of Images for the Product
    '''
    __tablename__ = "product"
    id:Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    shop_id:Mapped[int] = mapped_column(ForeignKey("shops.id"), type_=Integer)
    product_name:Mapped[str] = mapped_column(type_=Text)
    description:Mapped[str] = mapped_column(type_=VARCHAR(200))
    # relationships
    shop:Mapped["Shop"] = relationship(back_populates="prod")
    prod_image: Mapped[List['ProductImage']] = relationship(back_populates="prod", cascade="all, delete-orphan")