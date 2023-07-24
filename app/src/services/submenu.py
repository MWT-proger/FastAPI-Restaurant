import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from crud.submenu import CRUDSubmenu

from schemas.submenu import SubmenuCreate, SubmenuResponse, SubmenuUpdate
from core.deps import get_async_db
from services.base import ServiceBase

__all__ = (
    "SubmenuService",
    "get_service",
)


class SubmenuService(ServiceBase[SubmenuResponse, SubmenuUpdate]):
    obj_name = "submenu"
    
    async def get_list(self, menu_id: uuid.UUID) -> list[SubmenuResponse]:

        submenus: list = await self.crud.list(menu_id=menu_id)
        return submenus


    async def create(self, submenu_content: SubmenuCreate, menu_id: uuid.UUID) -> SubmenuResponse:
   

        submenu = await self.crud.add(submenu_content=submenu_content, menu_id=menu_id)
        return SubmenuResponse.from_orm(submenu)

    


async def get_service(
    session: AsyncSession = Depends(get_async_db),
) -> SubmenuService:
 
    crud = CRUDSubmenu(session)
    return SubmenuService(model=SubmenuResponse, crud=crud)
