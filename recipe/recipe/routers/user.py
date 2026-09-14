from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from recipe.database import get_db
from recipe.dependencies.auth import get_current_user
from recipe.models.user import User
from recipe.schemas.user import UserResponse, UserUpdate
from recipe.services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me",response_model=UserResponse)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me",response_model=UserResponse)
def update_my_profile(
    user_data: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):

    service = UserService(db)
    updated_user = service.update_user(
        current_user.user_id,
        user_data)

    return updated_user


@router.delete("/me",status_code=status.HTTP_204_NO_CONTENT)
def delete_my_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):

    service = UserService(db)

    service.delete_user(
        current_user.user_id)

    return None