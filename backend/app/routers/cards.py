from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import CardCreate, CardUpdate, CardOut
from app.services import card_service

router = APIRouter()


@router.post("", response_model=CardOut, status_code=201)
def create(data: CardCreate, db: Session = Depends(get_db)):
    return card_service.create_card(db, data.name)


@router.get("", response_model=list[CardOut])
def list_all(db: Session = Depends(get_db)):
    return card_service.list_cards(db)


@router.put("/{card_id}", response_model=CardOut)
def update(card_id: int, data: CardUpdate, db: Session = Depends(get_db)):
    return card_service.update_card(db, card_id, data.name)


@router.delete("/{card_id}", status_code=204)
def delete(card_id: int, db: Session = Depends(get_db)):
    card_service.delete_card(db, card_id)
