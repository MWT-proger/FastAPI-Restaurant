from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from repositories.base import AbstractRepository
from repositories.dish import DishRepository
from repositories.menu import MenuRepository
from repositories.submenu import SubmenuRepository


class AbstractRepositoriesContainer(ABC):
    menu_repo: AbstractRepository
    submenu_repo: AbstractRepository
    dish_repo: AbstractRepository


class RepositoriesContainer(AbstractRepositoriesContainer):
    """Контейнер для хранения всех репозиториев и сессий для работы с ними."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.menu_repo: MenuRepository = MenuRepository(session=self.session)
        self.submenu_repo: SubmenuRepository = SubmenuRepository(session=self.session)
        self.dish_repo: DishRepository = DishRepository(session=self.session)
