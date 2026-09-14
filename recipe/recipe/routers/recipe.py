from uuid import UUID 
from fastapi import APIRouter, Depends, Query, status 
from sqlalchemy.orm import Session 
from database import get_db 
from dependencies.auth import get_current_user 
from models.user import User 
from schemas.recipe import (RecipeCreate, RecipeResponse, RecipeUpdate) 
from services.recipe_service import RecipeService



router = APIRouter(
    prefix="/recipes",
    tags=["recipes"]
)


@router.get("/search") 
async def search_recipes( 
    query: str = Query( ..., min_length=1 ), 
    db: Session = Depends(get_db) ):
    
        service = RecipeService(db) 
        return await service.search_external( query ) 
        
        
        
        
@router.get("/random") 
async def random_recipe( db: Session = Depends(get_db) ): 
    service = RecipeService(db) 
    
    return await service.random_external() 
    
    
@router.get("/by-ingredient") 
async def recipes_by_ingredient( 
    ingredient: str = Query( ..., min_length=1 ), 
    db: Session = Depends(get_db) ): 
    
        service = RecipeService(db) 
        
        return await service.search_by_ingredient( ingredient ) 
        
        
@router.get("/external/{external_id}") 
async def get_external_recipe( external_id: str, db: Session = Depends(get_db) ): 
    service = RecipeService(db) 
    return await service.get_external( external_id ) 
    

@router.post( "", response_model=RecipeResponse, status_code=status.HTTP_201_CREATED ) 
def create_recipe(recipe_data: RecipeCreate, current_user: User = Depends( get_current_user ), 
db: Session = Depends(get_db) ): 

    service = RecipeService(db) 
    return service.create_recipe( recipe_data, current_user.user_id ) 
    
    
    
@router.get( "/mine", response_model=list[RecipeResponse] ) 
def get_my_recipes( current_user: User = Depends( get_current_user ), 
db: Session = Depends(get_db) ): 

    service = RecipeService(db) 
    return service.get_user_recipes( current_user.user_id ) 
    
    
    
    
@router.get( "/{recipe_id}", response_model=RecipeResponse ) 
def get_recipe( recipe_id: UUID, db: Session = Depends(get_db) ): 

    service = RecipeService(db) 
    return service.get_recipe( recipe_id ) 
    
    
    
    
@router.put( "/{recipe_id}", response_model=RecipeResponse ) 
def update_recipe( recipe_id: UUID, recipe_data: RecipeUpdate, current_user: User = Depends( get_current_user ), 
db: Session = Depends(get_db) ): 

    service = RecipeService(db) 
    return service.update_recipe( recipe_id, current_user.user_id, recipe_data ) 
    
    
    
    
@router.delete( "/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT ) 
def delete_recipe( recipe_id: UUID, current_user: User = Depends( get_current_user ), 
db: Session = Depends(get_db) ): 
    service = RecipeService(db) 
    service.delete_recipe( recipe_id, current_user.user_id ) 
    
    return None

