from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str = Field(...,min_length=3, max_length=50)
    description: str = Field(...,min_length=5, max_length=1000)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=3, max_length=1000)


class CategoryResponse(BaseModel):
    category_id: UUID   
    name: Optional[str]
    description: Optional[str]

    class Config:
        model_config = ConfigDict(from_attributes=True)
