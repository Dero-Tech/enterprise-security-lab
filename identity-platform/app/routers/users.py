from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[UserResponse])
def get_users():

    db: Session = SessionLocal()

    try:
        return db.query(User).all()
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):

    db: Session = SessionLocal()

    try:

        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            department=user.department,
            role=user.role,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    finally:
        db.close()


