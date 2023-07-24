from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.base import BaseModel, UUIDMixin


class Dish(BaseModel, UUIDMixin):
    """Модель блюда."""
    __tablename__ = "dishes"
    __table_args__ = ({"schema": "content"})

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    submenu_id = Column(UUID, ForeignKey("content.submenus.id", ondelete="CASCADE"), nullable=False)

    submenu = relationship("Submenu", back_populates="dishes")
