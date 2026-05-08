from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Card, Expense


def create_card(db: Session, name: str) -> Card:
    if db.query(Card).filter(Card.name == name).first():
        raise HTTPException(status_code=409, detail="카드 이름이 이미 존재합니다")
    card = Card(name=name)
    db.add(card)
    db.commit()
    db.refresh(card)
    return card


def list_cards(db: Session) -> list[Card]:
    return db.query(Card).order_by(Card.id).all()


def update_card(db: Session, card_id: int, name: str) -> Card:
    card = db.query(Card).get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="카드를 찾을 수 없습니다")
    if db.query(Card).filter(Card.name == name, Card.id != card_id).first():
        raise HTTPException(status_code=409, detail="카드 이름이 이미 존재합니다")
    card.name = name
    db.commit()
    db.refresh(card)
    return card


def delete_card(db: Session, card_id: int) -> None:
    card = db.query(Card).get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="카드를 찾을 수 없습니다")
    db.query(Expense).filter(Expense.card_id == card_id).update({"card_id": None})
    db.delete(card)
    db.commit()
