from uuid import UUID 
from fastapi import APIRouter, Depends, status 
from sqlalchemy.orm import Session 
from database import get_db 
from dependencies.auth import get_current_user 
from models.user import User
from models.favourite import Favourite 
from schemas.favourite import FavouriteResponse 
from services.favourite_service import FavouriteService 


router = APIRouter( prefix="/favourites", tags=["Favourites"] ) 



@router.post( "/{recipe_id}", response_model=FavouriteResponse, status_code=status.HTTP_201_CREATED ) 
def add_favourite( recipe_id: UUID, current_user: User = Depends( get_current_user ), db: Session = Depends(get_db) ): 
    service = FavouriteService(db) 
    return service.add( current_user.user_id, recipe_id ) 
    
    
    
    
@router.get( "", response_model=list[FavouriteResponse] ) 
def get_favourites( current_user: User = Depends( get_current_user ), db: Session = Depends(get_db) ): 
    service = FavouriteService(db) 
    
    return service.get_all(current_user.user_id) 
    
    
    
@router.delete( "/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT ) 
def remove_favourite( recipe_id: UUID, current_user: User = Depends( get_current_user ), db: Session = Depends(get_db) ): 
    service = FavouriteService(db) 
    service.remove( current_user.user_id, recipe_id ) 

    return {
        "message": "Favourite deleted successfully"
    }