from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repository.category_repository import CategoryRepository
from schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create(self, data: CategoryCreate):
        return self.repository.create(data)

    def get(self, category_id: UUID):
        category = self.repository.get(category_id)

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )

        return category

    def get_all(self):
        return self.repository.get_all()

    def update(self, category_id: UUID, data: CategoryUpdate):
        category = self.repository.update(category_id, data)

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )

        return category

    def delete(self, category_id: UUID):
        deleted = self.repository.delete(category_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )