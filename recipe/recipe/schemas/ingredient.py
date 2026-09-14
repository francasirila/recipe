from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import UUID



class IngredientBase(BaseModel):
    name: str | None
    quantity: str | None
    unit: str | None
    

class IngredientCreate(IngredientBase):
    pass

class IngredientResponse(BaseModel):
    ingredient_id: Optional[UUID]
    name: Optional[str]
    quantity: Optional[str] = None 
    unit: Optional[str] = None


    class Config:
        model_config = ConfigDict(from_attributes=True)

    

