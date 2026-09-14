from sqlalchemy.orm import Session
from uuid import UUID
from models.user import User
from schemas.user import UserCreate, UserResponse, UserUpdate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    
    def create_user(self,user_data: UserCreate,hashed_password: str) -> User:       
        user = User(username=user_data.username,email=user_data.email,hashed_password=hashed_password)

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    
    def get_user(self, user_id: UUID)-> User | None:
        return(
            self.db.query(User)
            .filter(
                User.user_id == user_id,
                User.is_active.is_(True))
            .first()
        )


    def get_user_by_email(self,email: str) -> User | None:
        return (self.db.query(User).filter(User.email == email).first())


    def get_user_by_username(self,username: str) -> User | None:
        return (self.db.query(User).filter(User.username == username).first())


    def get_all(self):
        return(self.db.query(User).filter(User.is_active.is_(True)).all())


    def update_user(self,user_id: UUID,user_data: UserUpdate) -> User | None:
        user = self.get_user(user_id)

        if user is None:
            return None

        update_data = user_data.model_dump(exclude_unset=True)

        if "password" in update_data:
            update_data.pop("password")

        for key, value in update_data.items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(db_user)

        return user

    def update_password(self,user_id: UUID,hashed_password: str) -> User | None:
        db_user = self.get_user(user_id)

        if db_user is None:
            return None

        db_user.hashed_password = hashed_password

        self.db.commit()
        self.db.refresh(db_user)
        
        return db_user

    def delete_user(self, user_id: UUID) -> User | None:
        db_user = self.get_user(user_id)

        if db_user is None:
            return None

        db_user.is_active = False

        self.db.commit()
        self.db.refresh(db_user)

        return db_user