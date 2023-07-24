import uuid

from fastapi import APIRouter, Body, Depends

from schemas.dish import (
    DishCreate,
    DishResponse,
    DishUpdate,
)
from services.dish import DishService, get_service

router = APIRouter()


@router.get(
    path="/{menu_id}/submenus/{submenu_id}/dishes",
    summary="Просмотр списка блюд",
    status_code=200,
)
async def get_list(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    dish_service: DishService = Depends(get_service),
) -> list[DishResponse]:
    dishes: list[DishResponse] = await dish_service.get_list(menu_id, submenu_id)
    return dishes


@router.get(
    path="/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    summary="Просмотр определенного блюда",
    status_code=200,
)
async def get(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    dish_id: uuid.UUID,
    dish_service: DishService = Depends(get_service),
) -> DishResponse:

    dish: DishResponse = await dish_service.get(dish_id)
    return dish


@router.post(
    path="/{menu_id}/submenus/{submenu_id}/dishes",
    summary="Создать блюдо",
    status_code=201,
)
async def create(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    dish_content: DishCreate = Body(None),
    dish_service: DishService = Depends(get_service),
) -> DishResponse:

    dish: DishResponse = await dish_service.create(menu_id, submenu_id, dish_content)
    return dish


@router.patch(
    path="/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    summary="Обновить блюдо",
    status_code=200,
)
async def patch(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    dish_id: uuid.UUID,
    dish_content: DishUpdate = Body(None),
    dish_service: DishService = Depends(get_service),
) -> DishResponse:

    dish: DishResponse = await dish_service.update(dish_id, dish_content)
    return dish


@router.delete(
    path="/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    summary="Удалить блюдо",
    status_code=200,
)
async def delete(
    menu_id: uuid.UUID,
    submenu_id: uuid.UUID,
    dish_id: uuid.UUID,
    dish_service: DishService = Depends(get_service),
) -> dict:
    dish: dict = await dish_service.delete(dish_id)
    return dish
