from uuid import uuid4

from sqlalchemy import String, Column,Integer,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    ingredient_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    recipe_id = Column( UUID(as_uuid=True), ForeignKey("recipes.recipe_id", ondelete="CASCADE"), nullable=False, index=True )    
    name = Column(String, nullable=False, index=True)
    quantity = Column(String, nullable=False, index=True)
    unit = Column(String, nullable=False, index=True)
    recipe = relationship("Recipe", back_populates="ingredients")
    

