from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import CategoryCreate, CategoryUpdate, CategoryOut
from app.services import category_service

router = APIRouter()


@router.post("", response_model=CategoryOut, status_code=201)
def create(data: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, data.name)


@router.get("", response_model=list[CategoryOut])
def list_all(db: Session = Depends(get_db)):
    return category_service.list_categories(db)


@router.put("/{category_id}", response_model=CategoryOut)
def update(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    return category_service.update_category(db, category_id, data.name)


@router.delete("/{category_id}", status_code=204)
def delete(category_id: int, db: Session = Depends(get_db)):
    category_service.delete_category(db, category_id)
