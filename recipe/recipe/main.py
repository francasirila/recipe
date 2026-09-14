from fastapi import FastAPI
from recipe.database import Base, engine
from recipe.models.user import User
from recipe.routers.auth import router as auth_router
from recipe.routers.user import router as users_router
from recipe.routers.recipe import router as recipe_router 
from recipe.routers.category import router as category_router 
from recipe.routers.favourite import router as favourite_router


app = FastAPI(
    title="Cookbook API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


app.include_router( auth_router ) 
app.include_router( users_router ) 
app.include_router( recipe_router ) 
app.include_router( category_router ) 
app.include_router( favourite_router )


@app.get("/")
def root():
    return {
        "message": "Recipe API is running"
    }