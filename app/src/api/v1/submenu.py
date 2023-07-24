import uuid

from fastapi import APIRouter, Body, Depends

from schemas.submenu import (
    SubmenuCreate,
    SubmenuResponse,
    SubmenuUpdate,
)
from services.submenu import SubmenuService, get_service

router = APIRouter()


@router.get(
    path="/{menu_id}/submenus",
    summary="Просмотр списка подменю",
    status_code=200,
)
async def get_list(
    menu_id: uuid.UUID,
    submenu_service: SubmenuService = Depends(get_service),
) -> list[SubmenuResponse]:
    submenus: list[SubmenuResponse] = await submenu_service.get_list(menu_id)
    return submenus


@router.get(
    path="/{menu_id}/submenus/{submenu_id}",
    summary="Просмотр определенного подменю",
    status_code=200,
)
async def get(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    submenu_service: SubmenuService = Depends(get_service),
) -> SubmenuResponse:
    submenu: SubmenuResponse = await submenu_service.get(submenu_id)
    return submenu


@router.post(
    path="/{menu_id}/submenus",
    summary="Создать подменю",
    status_code=201,
)
async def create(
    menu_id: uuid.UUID,
    submenu_content: SubmenuCreate = Body(None),
    submenu_service: SubmenuService = Depends(get_service),
) -> SubmenuResponse:
    submenu: SubmenuResponse = await submenu_service.create(submenu_content, menu_id)
    return submenu


@router.patch(
    path="/{menu_id}/submenus/{submenu_id}",
    summary="Обновить подменю",
    status_code=200,
)
async def patch(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    submenu_content: SubmenuUpdate = Body(None),
    submenu_service: SubmenuService = Depends(get_service),
) -> SubmenuResponse:
    submenu: SubmenuResponse = await submenu_service.update(submenu_id, submenu_content)
    return submenu


@router.delete(
    path="/{menu_id}/submenus/{submenu_id}",
    summary="Удалить подменю",
    status_code=200,
)
async def delete(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    submenu_service: SubmenuService = Depends(get_service),
) -> dict:
    submenu: dict = await submenu_service.delete(submenu_id)
    return submenu
