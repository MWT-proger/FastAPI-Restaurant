from typing import Any, Generic, List, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import BaseModel
from schemas.base import BaseSchema

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseSchema)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseSchema)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        obj = await db.scalars(select(self.model).filter_by(id=id))
        return obj.first()

    async def get_list(self, db: AsyncSession) -> Optional[ModelType]:
        obj = await db.scalars(select(self.model).all())
        return obj.first()

    async def create(self, db: AsyncSession, *, data: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(data)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @staticmethod
    async def update(db: AsyncSession, obj: ModelType,
                     update_data: UpdateSchemaType, field_none: List[str] = []) -> Optional[ModelType]:
        for column, value in update_data.dict(exclude_unset=True).items():
            if column in field_none:
                setattr(obj, column, value)
            elif value is not None:
                setattr(obj, column, value)
        await db.commit()
        await db.refresh(obj)
        return obj


crud_base = CRUDBase(BaseModel)
