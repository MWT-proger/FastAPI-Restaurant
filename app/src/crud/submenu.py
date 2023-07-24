import uuid

from sqlalchemy import func, select
from crud.base import CRUDBase

from schemas.submenu import SubmenuSchema
from models.submenu import Submenu

__all__ = ("CRUDSubmenu",)


class CRUDSubmenu(CRUDBase):
    model: type[Submenu] = Submenu

    async def list(self, menu_id: uuid.UUID) -> list[Submenu]:

        statement = (
            select(
                self.model.id,
                self.model.title,
                self.model.description,
                func.count(self.model.dishes).label("dishes_count"),
            )
            .outerjoin(self.model.dishes)
            .where(self.model.menu_id == menu_id)
            .group_by(self.model.id)
        )
        async with self.session as session:
            async with session.begin():
                try:
                    response = await session.execute(statement)
                except Exception:
                    pass
            submenus: list[Submenu] = response.fetchall()  # type: ignore
        return submenus

    async def get(self, submenu_id: uuid.UUID) -> Submenu | None:
  
        statement = (
            select(
                self.model.id,
                self.model.title,
                self.model.description,
                func.count(self.model.dishes).label("dishes_count"),
            )
            .outerjoin(
                self.model.dishes,
            )
            .where(
                self.model.id == submenu_id,
            )
            .group_by(self.model.id)
        )
        async with self.session as session:
            async with session.begin():
                try:
                    response = await session.execute(statement)
                except Exception:
                    pass
            submenu: Submenu | None = response.one_or_none()
        return submenu

    async def __get(self, submenu_id: uuid.UUID) -> Submenu | None:
        statement = select(self.model).where(self.model.id == submenu_id)
        async with self.session as session:
            async with session.begin():
                try:
                    response = await session.execute(statement)
                except Exception:
                    pass
        submenu: Submenu | None = response.scalar_one_or_none()
        return submenu

    async def add(self, submenu_content: SubmenuSchema, menu_id: uuid.UUID) -> Submenu | None:
  
        new_submenu = submenu_content.dict(exclude_unset=True)
        new_submenu["menu_id"] = menu_id
        submenu: Submenu = Submenu(**new_submenu)
        async with self.session as session:
            async with session.begin():
                try:
                    session.add(submenu)
                except Exception:
                    await session.rollback()
                else:
                    await session.commit()
            await session.refresh(submenu)
        return submenu

    async def update(self, submenu_id: uuid.UUID, submenu_content: SubmenuSchema) -> bool:

        submenu_status = False
        if submenu := await self.__get(submenu_id=submenu_id):
            updated_menu = submenu_content.dict(exclude_unset=True)
            for key, value in updated_menu.items():
                setattr(submenu, key, value)
            async with self.session as session:
                async with session.begin():
                    try:
                        session.add(submenu)
                        submenu_status = True
                    except Exception:
                        pass
                await session.refresh(submenu)
        return submenu_status

    async def delete(self, submenu_id: uuid.UUID) -> bool:

        submenu_status = False
        if submenu := await self.__get(submenu_id=submenu_id):
            async with self.session as session:
                async with session.begin():
                    try:
                        await session.delete(submenu)
                        await session.commit()
                        submenu_status = True
                    except Exception:
                        pass
        return submenu_status
