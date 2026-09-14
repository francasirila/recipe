from uuid import UUID 
from sqlalchemy.orm import Session 
from models.category import Category 
from schemas.category import (CategoryCreate, CategoryUpdate) 



class CategoryRepository: 
    def __init__(self, db: Session): 
        self.db = db 
        
        
    def create(self, data: CategoryCreate): 
        category = Category( 
            name=data.name, 
            description=data.description 
            ) 
            
            
        self.db.add(category) 
        self.db.commit() 
        self.db.refresh(category) 
        
        return category 
        
        
    def get( self, category_id: UUID ): 
        return ( self.db.query(Category) 
        .filter( Category.category_id == category_id ) 
        .first() )
        
        
    def get_all(self): 
        return ( self.db.query(Category) 
        .order_by(Category.name) .all() )
        


    def get_by_name(self, name):
        return self.db.query(Category).filter(Category.name == name).first()


        
    def update(self, category_id: UUID, data: CategoryUpdate): 
        category = self.get( category_id ) 
        
        
        
        if category is None: 
            return None 
            
            
        values = data.model_dump( exclude_unset=True ) 
            
            
        for key, value in values.items(): 
            setattr(category, key, value) 
            
            
            
            self.db.commit() 
            self.db.refresh(category) 
            
            
            return category 
            
    def delete(self, category_id: UUID):
        category = self.db.query(Category).filter(
            Category.category_id == category_id
        ).first()

        if category is None:
            return False

        self.db.delete(category)
        self.db.commit()

        return True