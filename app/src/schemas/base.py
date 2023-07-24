import uuid

from pydantic import BaseModel as Base
from pydantic import constr, validator


def set_price(cost: float) -> str:

    return f"{cost:.2f}"


class BaseSchema(Base):

    title: constr(min_length=2, max_length=30) 
    description: constr(min_length=2, max_length=255) 


    class Config:
        from_attributes = True

class BaseModel(Base):
    id: uuid.UUID
    title: str
    description: str

    class Config:
        from_attributes = True

class BaseMenu(BaseModel):
    submenus_count: int = 0
    dishes_count: int = 0

class BaseSubmenu(BaseModel):
    dishes_count: int = 0


class BaseDish(BaseModel):
    price: float
    _price = validator("price", allow_reuse=True)(set_price)
