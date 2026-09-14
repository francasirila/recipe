from fastapi import FastAPI
from database import Base, engine
from models.user import User
from routers.auth import router as auth_router
from routers.user import router as users_router
from routers.recipe import router as recipe_router 
from routers.category import router as category_router 
from routers.favourite import router as favourite_router


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
