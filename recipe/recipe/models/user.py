from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String, Column
from sqlalchemy.dialects.postgresql import UUID
from models.mfa import UserMFA
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    mfa_enabled = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    recipes = relationship( "Recipe", back_populates="user", cascade="all, delete-orphan" )
    favourites = relationship( "Favourite", back_populates="user", cascade="all, delete-orphan" )
    mfa = relationship("UserMFA",back_populates="user",cascade="all, delete-orphan")