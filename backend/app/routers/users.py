from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserCreate, UserUpdate, UserOut
from app.services import user_service

router = APIRouter()


@router.post("", response_model=UserOut, status_code=201)
def create(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, data.name)


@router.get("", response_model=list[UserOut])
def list_all(db: Session = Depends(get_db)):
    return user_service.list_users(db)


@router.put("/{user_id}", response_model=UserOut)
def update(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, data.name)


@router.delete("/{user_id}", status_code=204)
def delete(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
