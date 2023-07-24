import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud.menu import CRUDMenu
from schemas.menu import MenuCreate, MenuResponse, MenuUpdate
from core.deps import get_async_db
from services.base import ServiceBase

__all__ = (
    "MenuService",
    "get_service",
)


class MenuService(ServiceBase[MenuResponse, MenuUpdate]):
    obj_name = "menu"

    async def get_list(self) -> list[MenuResponse]:

        menus: list = await self.crud.list()
        return menus


    async def create(self, menu_content: MenuCreate) -> MenuResponse:


        menu = await self.crud.add(menu_content=menu_content)
        return MenuResponse.from_orm(menu)



async def get_service(
    session: AsyncSession = Depends(get_async_db),
) -> MenuService:
   
    crud = CRUDMenu(session)
    return MenuService(model=MenuResponse, crud=crud)
