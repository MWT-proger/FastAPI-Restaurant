from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import BaseModel, UUIDMixin


class Menu(BaseModel, UUIDMixin):
    """Модель меню."""

    __tablename__ = "menus"
    __table_args__ = ({"schema": "content"})

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    submenus = relationship("Submenu", back_populates="menu", cascade="all, delete")
