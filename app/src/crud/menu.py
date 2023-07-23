from crud.base import CRUDBase
from models import Menu
from schemas import CreateMenuSchema, UpdateMenuSchema


class CRUDMenu(CRUDBase[Menu, CreateMenuSchema, UpdateMenuSchema]):
    pass
