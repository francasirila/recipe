from uuid import UUID 
from fastapi import HTTPException, status 
from sqlalchemy.orm import Session 
from models.ingredient import Ingredient 
from models.recipe import Recipe 
from repository.recipe_repository import RecipeRepository 
from schemas.recipe import RecipeCreate, RecipeResponse, RecipeUpdate 
from services.external_recipe import themealdb_provider 





class RecipeService: 
    def __init__(self, db: Session): 
        self.db = db 
        self.repository = RecipeRepository(db) 
        


    async def search_external(self, query: str): 
        return await themealdb_provider.search(query) 



    async def get_external(self, external_id: str): 
        recipe = ( await themealdb_provider.get_by_id( external_id ) ) 
        
        if recipe is None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            
            detail="Recipe not found") 
            
        return recipe 



    async def random_external(self): 
        recipe = (await themealdb_provider.random()) 
        
        if recipe is None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No recipe found") 
            
        return recipe 
            
            
    async def search_by_ingredient(self, ingredient: str ):
        return ( await themealdb_provider .search_by_ingredient( ingredient ) ) 

from uuid import UUID 
from fastapi import HTTPException, status 
from sqlalchemy.orm import Session 
from models.ingredient import Ingredient 
from models.recipe import Recipe 
from repository.recipe_repository import RecipeRepository 
from schemas.recipe import RecipeCreate, RecipeResponse, RecipeUpdate 
from services.external_recipe import themealdb_provider 





class RecipeService: 
    def __init__(self, db: Session): 
        self.db = db 
        self.repository = RecipeRepository(db) 
        


    async def search_external(self, query: str): 
        return await themealdb_provider.search(query) 



    async def get_external(self, external_id: str): 
        recipe = ( await themealdb_provider.get_by_id( external_id ) ) 
        
        if recipe is None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            
            detail="Recipe not found") 
            
        return recipe 



    async def random_external(self): 
        recipe = (await themealdb_provider.random()) 
        
        if recipe is None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No recipe found") 
            
        return recipe 
            
            
    async def search_by_ingredient(self, ingredient: str ):
        return ( await themealdb_provider .search_by_ingredient( ingredient ) ) 



    def create_recipe(self, recipe_data: RecipeCreate, user_id: UUID):
        from models.category import Category

        category = self.db.query(Category).filter(
            Category.name == recipe_data.category
        ).first()

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )

        return self.repository.create_recipe(
            recipe_data,
            user_id,
            category.category_id
        )   


    def get_recipe( self, recipe_id: UUID ): 
        recipe = self.repository.get_recipe( recipe_id ) 
        
        if recipe is None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found") 
            
        return recipe 
            
            
            
    def get_user_recipes( self, user_id: UUID ): 
        return self.repository.get_user_recipes( user_id ) 
        
        
    def update_recipe( self, recipe_id: UUID, user_id: UUID, recipe_data: RecipeUpdate ): 
        recipe = self.repository.update_recipe( recipe_id, user_id, recipe_data ) 
        
        if recipe is None: 
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found" ) 
            
        return recipe 
            
    
    def delete_recipe( self, recipe_id: UUID, user_id: UUID ): 
        deleted = self.repository.delete_recipe( recipe_id, user_id ) 
        
        if not deleted: 
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")


    def get_recipe( self, recipe_id: UUID ): 
        recipe = self.repository.get_recipe( recipe_id ) 
        
        if recipe is None: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found") 
            
        return recipe 
            
            
            
    def get_user_recipes( self, user_id: UUID ): 
        return self.repository.get_user_recipes( user_id ) 
        
        
    def update_recipe( self, recipe_id: UUID, user_id: UUID, recipe_data: RecipeUpdate ): 
        recipe = self.repository.update_recipe( recipe_id, user_id, recipe_data ) 
        
        if recipe is None: 
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found" ) 
            
        return recipe 
            
    
    def delete_recipe( self, recipe_id: UUID, user_id: UUID ): 
        deleted = self.repository.delete_recipe( recipe_id, user_id ) 
        
        if not deleted: 
            raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")