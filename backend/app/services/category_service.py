from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Category, Expense


def create_category(db: Session, name: str) -> Category:
    if db.query(Category).filter(Category.name == name).first():
        raise HTTPException(status_code=409, detail="카테고리 이름이 이미 존재합니다")
    cat = Category(name=name)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


def list_categories(db: Session) -> list[Category]:
    return db.query(Category).order_by(Category.id).all()


def update_category(db: Session, category_id: int, name: str) -> Category:
    cat = db.query(Category).get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="카테고리를 찾을 수 없습니다")
    if db.query(Category).filter(Category.name == name, Category.id != category_id).first():
        raise HTTPException(status_code=409, detail="카테고리 이름이 이미 존재합니다")
    cat.name = name
    db.commit()
    db.refresh(cat)
    return cat


def delete_category(db: Session, category_id: int) -> None:
    cat = db.query(Category).get(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="카테고리를 찾을 수 없습니다")
    if cat.name == "기타" and cat.is_default:
        raise HTTPException(status_code=400, detail="기타 카테고리는 삭제할 수 없습니다")
    default_cat = db.query(Category).filter(Category.name == "기타", Category.is_default == True).first()
    if default_cat:
        db.query(Expense).filter(Expense.category_id == category_id).update({"category_id": default_cat.id})
    db.delete(cat)
    db.commit()
