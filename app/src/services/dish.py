import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud.dish import CRUDDish
from schemas.dish import DishCreate, DishResponse, DishUpdate
from core.deps import get_async_db
from services.base import ServiceBase


class DishService(ServiceBase[DishResponse, DishUpdate]):
    obj_name = "dish"

    async def get_list(self, menu_id: uuid.UUID, submenu_id: uuid.UUID) -> list[DishResponse]:

        dishes: list = await self.crud.list(submenu_id=submenu_id)
        dishes = [DishResponse.from_orm(dish) for dish in dishes]
        return dishes


    async def create(
        self,
        menu_id: uuid.UUID,
        submenu_id: uuid.UUID,
        dish_content: DishCreate,
    ) -> DishResponse:

        dish = await self.crud.add(dish_content=dish_content, submenu_id=submenu_id)
        return DishResponse.from_orm(dish)


async def get_service(
    session: AsyncSession = Depends(get_async_db),
) -> DishService:

    crud = CRUDDish(session=session)
    return DishService(model=DishResponse, crud=crud)
