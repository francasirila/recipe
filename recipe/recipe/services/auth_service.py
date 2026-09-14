from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repository.user_repository import UserRepository
from schemas.auth import LoginRequest
from security.jwt import (
    create_access_token,
    create_mfa_challenge_token,
    create_refresh_token
)
from security.password import verify_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def login(self, login_data: LoginRequest):

        user = self.repository.get_user_by_email(
            login_data.email
        )

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive"
            )

        password_valid = verify_password(
            login_data.password,
            user.hashed_password
        )

        if not password_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        user.last_login = datetime.now(timezone.utc)

        self.db.commit()

        if user.mfa_enabled:

            challenge_token = create_mfa_challenge_token(
                user.user_id
            )

            return {
                "mfa_required": True,
                "challenge_token": challenge_token,
                "token_type": "bearer"
            }

        access_token = create_access_token(
            user.user_id
        )

        refresh_token = create_refresh_token(
            user.user_id
        )

        return {
            "mfa_required": False,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }