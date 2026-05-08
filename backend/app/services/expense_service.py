from fastapi import HTTPException
from sqlalchemy import extract
from sqlalchemy.orm import Session

from app.models import Expense, Card, Category, User


def create_expense(db: Session, data: dict) -> Expense:
    if data.get("card_id") and not db.query(Card).get(data["card_id"]):
        raise HTTPException(status_code=400, detail="존재하지 않는 카드입니다")
    if data.get("category_id") and not db.query(Category).get(data["category_id"]):
        raise HTTPException(status_code=400, detail="존재하지 않는 카테고리입니다")
    if data.get("user_id") and not db.query(User).get(data["user_id"]):
        raise HTTPException(status_code=400, detail="존재하지 않는 사용자입니다")
    expense = Expense(**data)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def list_expenses(db: Session, year: int, month: int, category_id: int | None = None, card_id: int | None = None, user_id: int | None = None) -> list[dict]:
    q = db.query(Expense).filter(
        extract("year", Expense.date) == year,
        extract("month", Expense.date) == month,
    )
    if category_id:
        q = q.filter(Expense.category_id == category_id)
    if card_id:
        q = q.filter(Expense.card_id == card_id)
    if user_id:
        q = q.filter(Expense.user_id == user_id)
    expenses = q.order_by(Expense.date.desc(), Expense.id.desc()).all()

    result = []
    for e in expenses:
        card = db.query(Card).get(e.card_id) if e.card_id else None
        cat = db.query(Category).get(e.category_id) if e.category_id else None
        user = db.query(User).get(e.user_id) if e.user_id else None
        result.append({
            "id": e.id,
            "date": e.date,
            "amount": e.amount,
            "memo": e.memo,
            "card_id": e.card_id,
            "category_id": e.category_id,
            "user_id": e.user_id,
            "card_name": card.name if card else None,
            "category_name": cat.name if cat else None,
            "user_name": user.name if user else None,
            "created_at": e.created_at,
        })
    return result


def update_expense(db: Session, expense_id: int, data: dict) -> Expense:
    expense = db.query(Expense).get(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="소비 내역을 찾을 수 없습니다")
    if data.get("card_id") and not db.query(Card).get(data["card_id"]):
        raise HTTPException(status_code=400, detail="존재하지 않는 카드입니다")
    if data.get("category_id") and not db.query(Category).get(data["category_id"]):
        raise HTTPException(status_code=400, detail="존재하지 않는 카테고리입니다")
    if data.get("user_id") and not db.query(User).get(data["user_id"]):
        raise HTTPException(status_code=400, detail="존재하지 않는 사용자입니다")
    for key, value in data.items():
        if value is not None:
            setattr(expense, key, value)
    db.commit()
    db.refresh(expense)
    return expense


def delete_expense(db: Session, expense_id: int) -> None:
    expense = db.query(Expense).get(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="소비 내역을 찾을 수 없습니다")
    db.delete(expense)
    db.commit()
