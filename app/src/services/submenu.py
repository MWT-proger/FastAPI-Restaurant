import uuid

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.schemas.submenu import SubmenuCreate, SubmenuResponse, SubmenuUpdate
from core.deps import get_async_db
from repositories.container import RepositoriesContainer
from services.mixin import ServiceMixin

__all__ = (
    "SubmenuService",
    "get_submenu_service",
)


class SubmenuService(ServiceMixin):
    async def get_submenus(self, menu_id: uuid.UUID) -> list[SubmenuResponse]:
        """Возвращает список всех подменю, принадлежащих меню по `id` меню.

        :param menu_id: Идентификатор меню.
        """

        submenus: list = await self.container.submenu_repo.list(menu_id=menu_id)
        return submenus

    async def get_submenu(self, submenu_id: uuid.UUID, menu_id: uuid.UUID) -> SubmenuResponse:
        """Возвращает подменю в меню по его `id`.

        :param submenu_id: Идентификатор подменю.
        :param menu_id: Идентификатор меню.
        """

        if submenu := await self.container.submenu_repo.get(submenu_id=submenu_id):
            submenu = SubmenuResponse.from_orm(submenu)

            return submenu
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found")

    async def create_submenu(self, submenu_content: SubmenuCreate, menu_id: uuid.UUID) -> SubmenuResponse:
        """Создает новое подменю в меню.

        :param submenu_content: Поля для создания подменю.
        :param menu_id: Идентификатор меню.
        """

        submenu = await self.container.submenu_repo.add(submenu_content=submenu_content, menu_id=menu_id)
        return SubmenuResponse.from_orm(submenu)

    async def update_submenu(
        self,
        submenu_id: uuid.UUID,
        submenu_content: SubmenuUpdate,
        menu_id: uuid.UUID,
    ) -> SubmenuResponse:
        """Обновляет подменю в меню.

        :param submenu_id: Идентификатор подменю.
        :param submenu_content: Поля для обновления подменю.
        :param menu_id: Идентификатор меню.
        """
        submenu_status: bool = await self.container.submenu_repo.update(
            submenu_id=submenu_id, submenu_content=submenu_content
        )
        if submenu_status is True:
            submenu = await self.container.submenu_repo.get(submenu_id)
            submenu = SubmenuResponse.from_orm(submenu)

            return submenu
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found")

    async def delete_submenu(self, submenu_id: uuid.UUID, menu_id: uuid.UUID) -> dict:
        """Удаляет подменю из меню по его `id`.

        :param submenu_id: Идентификатор подменю.
        :param menu_id: Идентификатор меню.
        """
        submenu_status: bool = await self.container.submenu_repo.delete(submenu_id=submenu_id)
        if submenu_status is True:
            return {
                "status": submenu_status,
                "message": "The submenu has been deleted",
            }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found")


async def get_submenu_service(
    session: AsyncSession = Depends(get_async_db),
) -> SubmenuService:
    """Функция для внедрения зависимостей.

    :param cache: Кеш.
    :param session: Сессия с базой данных.
    """
    container = RepositoriesContainer(session=session)
    return SubmenuService(container=container)
