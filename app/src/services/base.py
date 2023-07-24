from typing import Generic, TypeVar, Type
from dataclasses import dataclass
from fastapi import HTTPException, status
import uuid

from pydantic import BaseModel


ResponseModel = TypeVar("ResponseModel", bound=BaseModel)
ModelUpdate = TypeVar("ModelUpdate", bound=BaseModel)

@dataclass
class ServiceBase(Generic[ResponseModel, ModelUpdate]):
    obj_name = "obj"

    def __init__(self, model: Type[ResponseModel], crud):
        self.model = model
        self.crud = crud

    async def get(self, obj_id: uuid.UUID) -> ResponseModel:


        if obj := await self.crud.get(obj_id):
            obj = self.model.from_orm(obj)
            return obj
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.obj_name} not found")
    
    async def update(
        self,
        obj_id: uuid.UUID,
        obj_content: ModelUpdate,
    ) -> ResponseModel:
   
        obj_status: bool = await self.crud.update(obj_id, obj_content)

        if obj_status is True:
            obj = await self.crud.get(obj_id)
            obj = self.model.from_orm(obj)

            return obj
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.obj_name} not found")

    async def delete(self, obj_id: uuid.UUID) -> dict:
    
        status: bool = await self.crud.delete(obj_id)
        if status is True:
            return {
                "status": status,
                "message": f"The {self.obj_name} has been deleted",
            }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.obj_name} not found")
