from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    name = Column (String, unique=True, index=True)
    description = Column( String(1000), nullable=True )
    recipes = relationship("Recipe", back_populates="category")

