from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.auth import LoginRequest
from schemas.user import UserCreate, UserResponse
from services.auth_service import AuthService
from services.user_service import UserService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user_data)


@router.post("/login")
def login(login_data: LoginRequest,db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(login_data)