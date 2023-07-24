import uuid

from fastapi import APIRouter, Body, Depends

from schemas.menu import (
    MenuCreate,
    MenuResponse,
    MenuUpdate,
)
from services.menu import MenuService, get_service

router = APIRouter()


@router.get(
    path="/",
    summary="Просмотр списка меню",
    status_code=200,
)
async def get_list(
    menu_service: MenuService = Depends(get_service),
) -> list[MenuResponse]:
    menus: list[MenuResponse] = await menu_service.get_list()
    return menus


@router.get(
    path="/{menu_id}",
    summary="Просмотр определенного меню",
    status_code=200,
)
async def get(menu_id: uuid.UUID, menu_service: MenuService = Depends(get_service)) -> MenuResponse:
    menu: MenuResponse = await menu_service.get(menu_id)
    return menu


@router.post(
    path="/",
    summary="Создать меню",
    status_code=201,
)
async def create(
    menu_content: MenuCreate = Body(None),
    menu_service: MenuService = Depends(get_service),
) -> MenuResponse:
    menu: MenuResponse = await menu_service.create(menu_content)
    return menu


@router.patch(
    path="/{menu_id}",
    summary="Обновить меню",
    status_code=200,
)
async def patch(
    menu_id: uuid.UUID,
    menu_content: MenuUpdate = Body(None),
    menu_service: MenuService = Depends(get_service),
) -> MenuResponse:
    menu: MenuResponse = await menu_service.update(menu_id, menu_content)
    return menu


@router.delete(
    path="/{menu_id}",
    summary="Удалить меню",
    status_code=200,
)
async def delete(menu_id: uuid.UUID, menu_service: MenuService = Depends(get_service)) -> dict:
    menu: dict = await menu_service.delete(menu_id)
    return menu
