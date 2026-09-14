from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repository.user_repository import UserRepository
from schemas.user import UserCreate, UserUpdate
from security.password import hash_password


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(
        self,
        user_data: UserCreate
    ):

        existing_email = self.repository.get_user_by_email(
            user_data.email
        )

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email is already registered"
            )

        existing_username = (
            self.repository.get_user_by_username(
                user_data.username
            ))

        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username is already taken"
            )

        hashed_password = hash_password(
            user_data.password
        )

        return self.repository.create_user(
            user_data,
            hashed_password
        )

    def get_user(self, user_id: UUID):

        user = self.repository.get_user(user_id)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    def update_user(
        self,
        user_id: UUID,
        user_data: UserUpdate
    ):

        return self.repository.update_user(
            user_id,
            user_data
        )

    def delete_user(
        self,
        user_id: UUID
    ):

        return self.repository.delete_user(
            user_id
        )