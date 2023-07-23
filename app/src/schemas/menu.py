import uuid

from schemas import BaseSchema, BaseResponse


class MenuSchema(BaseSchema):
    id: uuid.UUID
    title: str
    description: str
    submenus_count: int = 0
    dishes_count: int = 0


class MenuResponse(BaseResponse):
    pass


class CreateMenuSchema(MenuSchema):
    title: str
    description: str


class UpdateMenuSchema(MenuSchema):
    title: str
    description: str
