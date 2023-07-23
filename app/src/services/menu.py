import uuid

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.schemas.menu import MenuCreate, MenuResponse, MenuUpdate
from core.deps import get_async_db
from repositories.container import RepositoriesContainer
from services.mixin import ServiceMixin

__all__ = (
    "MenuService",
    "get_menu_service",
)


class MenuService(ServiceMixin):
    async def get_menus(self) -> list[MenuResponse]:
        """Возвращает список всех меню."""

        menus: list = await self.container.menu_repo.list()
        return menus

    async def get_menu(self, menu_id: uuid.UUID) -> MenuResponse:
        """Возвращает меню по его `id`.

        :param menu_id: Идентификатор меню.
        """

        if menu := await self.container.menu_repo.get(menu_id=menu_id):
            menu = MenuResponse.from_orm(menu)
            return menu
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")

    async def create_menu(self, menu_content: MenuCreate) -> MenuResponse:
        """Создает новое меню.

        :param menu_content: Поля для создания меню.
        """

        menu = await self.container.menu_repo.add(menu_content=menu_content)
        return MenuResponse.from_orm(menu)

    async def update_menu(self, menu_id: uuid.UUID, menu_content: MenuUpdate) -> MenuResponse:
        """Обновляет меню.

        :param menu_id: Идентификатор меню.
        :param menu_content: Поля для обновления меню.
        """
        menu_status: bool = await self.container.menu_repo.update(menu_id=menu_id, menu_content=menu_content)
        if menu_status is True:
            menu = await self.container.menu_repo.get(menu_id)
            menu = MenuResponse.from_orm(menu)
            return menu
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")

    async def delete_menu(self, menu_id: uuid.UUID) -> dict:
        """Удаляет меню по его `id`.

        :param menu_id: Идентификатор меню.
        """
        menu_status: bool = await self.container.menu_repo.delete(menu_id=menu_id)
        if menu_status is True:
            return {
                "status": menu_status,
                "message": "The menu has been deleted",
            }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")


async def get_menu_service(
    session: AsyncSession = Depends(get_async_db),
) -> MenuService:
    """Функция для внедрения зависимостей.

    :param cache: Кеш.
    :param session: Сессия с базой данных.
    """
    container = RepositoriesContainer(session=session)
    return MenuService(container=container)
