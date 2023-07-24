from schemas.base import BaseDish, BaseSchema


class DishSchema(BaseSchema):
    price: float


class DishUpdate(DishSchema):
    pass


class DishCreate(DishSchema):
    pass


class DishResponse(BaseDish):
    pass
