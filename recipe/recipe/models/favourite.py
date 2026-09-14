from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String, Column,ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Favourite(Base):
    __tablename__ = "favourites"

    favourite_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), index=True)
    recipe_id = Column(UUID(as_uuid=True),ForeignKey("recipes.recipe_id"), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    user = relationship( "User", back_populates="favourites" ) 
    recipe = relationship( "Recipe", back_populates="favourites" ) 
    
    __table_args__ = (UniqueConstraint( "user_id", "recipe_id", name="uq_user_recipe_favourite" ), )