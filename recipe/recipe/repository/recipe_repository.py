from uuid import UUID
from sqlalchemy.orm import Session
from models.ingredient import Ingredient
from models.recipe import Recipe
from schemas.recipe import RecipeCreate, RecipeUpdate

class RecipeRepository: 
    def __init__(self, db: Session): 
        self.db = db 
            
    def create_recipe(self,recipe_data: RecipeCreate,user_id: UUID,category_id: UUID) -> Recipe:
        recipe = Recipe(
            user_id=user_id,
            category_id=category_id,
            name=recipe_data.name,
            description=recipe_data.description,
            instructions=recipe_data.instructions,
            image_url=recipe_data.image_url,
            prep_time=recipe_data.prep_time,
            cook_time=recipe_data.cook_time,
            servings=recipe_data.servings,
            cuisine=recipe_data.cuisine,
            source="local"
        )

        self.db.add(recipe)
        self.db.flush()

        for ingredient_data in recipe_data.ingredients:
            ingredient = Ingredient(
                recipe_id=recipe.recipe_id,
                name=ingredient_data.name,
                quantity=ingredient_data.quantity,
                unit=ingredient_data.unit
            )

            self.db.add(ingredient)

        self.db.commit()
        self.db.refresh(recipe)

        return recipe

    def get_recipe( self, recipe_id: UUID ) -> Recipe | None: 
        return ( 
            self.db.query(Recipe) 
            .filter(Recipe.recipe_id == recipe_id) 
            .first() 
            )


    def get_user_recipe( self, recipe_id: UUID, user_id: UUID ) -> Recipe | None: 
        return ( 
            self.db.query(Recipe) 
            .filter( 
                Recipe.recipe_id == recipe_id, 
                Recipe.user_id == user_id ) 
            .first() 
            ) 
            
    def get_user_recipes( self, user_id: UUID ) -> list[Recipe]: 
        return ( self.db.query(Recipe) 
        .filter(Recipe.user_id == user_id) 
        .all() 
        ) 
        
        
    def update_recipe( self, recipe_id: UUID, user_id: UUID, recipe_data: RecipeUpdate ) -> Recipe | None: 
        recipe = self.get_user_recipe( recipe_id, user_id ) 
        
        if recipe is None: 
            return None 
            data = recipe_data.model_dump( exclude_unset=True ) 
            ingredients = data.pop( "ingredients", None ) 
            
        for key, value in data.items(): 
            setattr(recipe, key, value) 
            
        if ingredients is not None: 
            recipe.ingredients.clear() 
            
        for ingredient_data in ingredients: 
            recipe.ingredients.append( 
                Ingredient( 
                    name=ingredient_data.name, 
                    quantity=ingredient_data.quantity, 
                    unit=ingredient_data.unit ) ) 
                    
                    
        self.db.commit() 
        self.db.refresh(recipe) 
        
        return recipe 
        
    def delete_recipe( self, recipe_id: UUID, user_id: UUID ) -> bool: 
        recipe = self.get_user_recipe( recipe_id, user_id ) 
        if recipe is None: 
            return False 
            
            self.db.delete(recipe) 
            
            self.db.commit() 
            return True 
    def find_external_recipe(self, external_id: str, source: str) -> Recipe | None: 
        return ( self.db.query(Recipe) 
        .filter( Recipe.external_id == external_id, Recipe.source == source ) 
        .first()
         )