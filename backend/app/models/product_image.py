from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, Integer, ForeignKey
from ..db.base import Base
# ---------------------------------------Product Image--------------------------------------------------
if TYPE_CHECKING:
    from .product import Product
class ProductImage(Base):
    __tablename__ = "product_image"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    image_url: Mapped[str] = mapped_column(type_=Text)
    prod: Mapped["Product"] = relationship(back_populates="prod_image")
