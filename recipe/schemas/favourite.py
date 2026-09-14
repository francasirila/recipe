from datetime import datetime 
from uuid import UUID 
from pydantic import BaseModel, ConfigDict 
from schemas.recipe import RecipeResponse 





class FavouriteResponse(BaseModel): 
    favourite_id: UUID 
    recipe_id: UUID 
    created_at: datetime 
    recipe: RecipeResponse


    class Config:
        model_config = ConfigDict(from_attributes=True) 
