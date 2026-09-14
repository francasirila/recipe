from uuid import UUID 
from sqlalchemy.orm import Session 
from models.favourite import Favourite 




class FavouriteRepository: 
    def __init__(self, db: Session): 
        self.db = db 



    def get( self, user_id: UUID, recipe_id: UUID ): 
        return ( self.db.query(Favourite) 
        .filter( Favourite.user_id == user_id, 
        Favourite.recipe_id == recipe_id ) 
        .first() ) 
        
        
    def create( self, user_id: UUID, recipe_id: UUID ): 
        favourite = Favourite( user_id=user_id, recipe_id=recipe_id ) 

        self.db.add(favourite) 
        self.db.commit() 
        self.db.refresh(favourite) 
        return favourite 
        
        
    def get_user_favourites( self, user_id: UUID ): 
        return ( self.db.query(Favourite) 
        .filter( Favourite.user_id == user_id ) 
        .all() ) 
        
        
        
    def delete( self, favourite: Favourite ): 
        self.db.delete(favourite) 
        self.db.commit()