from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
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

