from uuid import UUID 
from fastapi import HTTPException, status 
from sqlalchemy.orm import Session 
from models.recipe import Recipe 
from repository.favourite_repository import (FavouriteRepository) 



class FavouriteService: 
    def __init__(self, db: Session): 
        self.db = db 
        self.repository = FavouriteRepository( db ) 
        
        
        
    def add( self, user_id: UUID, recipe_id: UUID ): 
        recipe = ( self.db.query(Recipe) 
        .filter( Recipe.recipe_id == recipe_id ) 
        .first() ) 
        
        
        if recipe is None: 
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found" ) 
        
        existing = self.repository.get( user_id, recipe_id ) 
            


        if existing: 
            raise HTTPException( status_code=status.HTTP_409_CONFLICT, detail="Recipe is already in favourites" ) 
        
        return self.repository.create( user_id, recipe_id ) 
            
                
                
    def get_all( self, user_id: UUID ): 
        return self.repository.get_user_favourites( user_id ) 
        
        
        
    def remove( self, user_id: UUID, recipe_id: UUID ): 
        favourite = self.repository.get( user_id, recipe_id ) 
        
        if favourite is None: 
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Favourite not found" ) 
        self.repository.delete( favourite )