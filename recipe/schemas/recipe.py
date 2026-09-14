from uuid import UUID 
from pydantic import BaseModel, ConfigDict, Field 
from schemas.ingredient import IngredientCreate, IngredientResponse 


class RecipeCreate(BaseModel): 
    name: str = Field( ..., min_length=2, max_length=255 ) 
    description: str | None = None 
    instructions: str = Field( ..., min_length=1 ) 
    image_url: str | None = None 
    prep_time: int | None = Field( None, ge=0 ) 
    cook_time: int | None = Field( None, ge=0 ) 
    servings: int | None = Field( None, ge=1 ) 
    cuisine: str | None = None 
    category: str | None = None 
    ingredients: list[IngredientCreate] = [] 
    
    
    
class RecipeUpdate(BaseModel): 
    name: str | None = Field( None, min_length=2, max_length=255 ) 
    description: str | None = None 
    instructions: str | None = None 
    image_url: str | None = None 
    prep_time: int | None = Field( None, ge=0 ) 
    cook_time: int | None = Field( None, ge=0 ) 
    servings: int | None = Field( None, ge=1 ) 
    cuisine: str | None = None 
    category_id: UUID | None = None 
    ingredients: list[IngredientCreate] | None = None 
    
    
    
class RecipeResponse(BaseModel): 
    
    recipe_id: UUID 
    user_id: UUID | None 
    category_id: UUID | None 
    external_id: str | None =None
    source: str 
    name: str 
    description: str | None 
    instructions: str | None 
    image_url: str | None 
    prep_time: int | None 
    cook_time: int | None 
    servings: int | None 
    cuisine: str | None 
    video_url: str | None =None
    ingredients: list[IngredientResponse]


    class Config:
        model_config = ConfigDict(from_attributes=True) 
