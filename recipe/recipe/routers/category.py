from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.auth import get_current_user
from models.user import User
from schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from services.category_service import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@router.get("", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    service = CategoryService(db)

    return service.get_all()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: UUID,
    db: Session = Depends(get_db)):
    service = CategoryService(db)

    return service.get(category_id)


@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    data: CategoryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    service = CategoryService(db)

    return service.create(data)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: UUID,
    data: CategoryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    service = CategoryService(db)

    return service.update(category_id, data)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    service = CategoryService(db)

    service.delete(category_id)

    return {
        "message": "Category deleted successfully"
    }