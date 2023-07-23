from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.base import BaseModel, UUIDMixin


class Submenu(BaseModel, UUIDMixin):
    """Модель подменю."""

    __tablename__ = "submenus"
    __table_args__ = ({"schema": "content"})

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    menu_id = Column(UUID, ForeignKey("content.menus.id", ondelete="CASCADE"), nullable=False)

    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete")
