from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String, Column,Integer,ForeignKey,Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    recipe_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    category_id = Column( UUID(as_uuid=True), ForeignKey("categories.category_id", ondelete="SET NULL"), nullable=True, index=True )    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), index=True)
    name = Column(String, nullable=False, index=True)
    description = Column (String, unique=True, index=True)
    source = Column(String(30), nullable=False, default="local")
    instructions = Column(Text, nullable=False)
    image_url = Column( String(1000), nullable=True )
    prep_time = Column( Integer, nullable=True)
    cook_time = Column( Integer, nullable=True)
    servings = Column (Integer,index=True)
    cuisine = Column (String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship( "User", back_populates="recipes" ) 
    category = relationship( "Category", back_populates="recipes" ) 
    ingredients = relationship( "Ingredient", back_populates="recipe", cascade="all, delete-orphan" )
    favourites = relationship( "Favourite", back_populates="recipe", cascade="all, delete-orphan" )
