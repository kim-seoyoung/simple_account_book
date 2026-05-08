from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User, Expense


def create_user(db: Session, name: str) -> User:
    if db.query(User).filter(User.name == name).first():
        raise HTTPException(status_code=409, detail="사용자 이름이 이미 존재합니다")
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session) -> list[User]:
    return db.query(User).order_by(User.id).all()


def update_user(db: Session, user_id: int, name: str) -> User:
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    if db.query(User).filter(User.name == name, User.id != user_id).first():
        raise HTTPException(status_code=409, detail="사용자 이름이 이미 존재합니다")
    user.name = name
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> None:
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    db.query(Expense).filter(Expense.user_id == user_id).update({"user_id": None})
    db.delete(user)
    db.commit()
