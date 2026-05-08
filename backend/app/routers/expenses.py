from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ExpenseCreate, ExpenseUpdate, ExpenseOut
from app.services import expense_service

router = APIRouter()


@router.post("", response_model=ExpenseOut, status_code=201)
def create(data: ExpenseCreate, db: Session = Depends(get_db)):
    expense = expense_service.create_expense(db, data.model_dump(exclude_unset=True))
    return expense_service.list_expenses(db, data.date.year, data.date.month)[-1] if False else _to_out(expense, db)


@router.get("", response_model=list[ExpenseOut])
def list_all(
    year: int = Query(...),
    month: int = Query(...),
    category_id: int | None = None,
    card_id: int | None = None,
    user_id: int | None = None,
    db: Session = Depends(get_db),
):
    return expense_service.list_expenses(db, year, month, category_id, card_id, user_id)


@router.put("/{expense_id}", response_model=ExpenseOut)
def update(expense_id: int, data: ExpenseUpdate, db: Session = Depends(get_db)):
    expense = expense_service.update_expense(db, expense_id, data.model_dump(exclude_unset=True))
    return _to_out(expense, db)


@router.delete("/{expense_id}", status_code=204)
def delete(expense_id: int, db: Session = Depends(get_db)):
    expense_service.delete_expense(db, expense_id)


def _to_out(expense, db):
    from app.models import Card, Category, User
    card = db.query(Card).get(expense.card_id) if expense.card_id else None
    cat = db.query(Category).get(expense.category_id) if expense.category_id else None
    user = db.query(User).get(expense.user_id) if expense.user_id else None
    return {
        "id": expense.id,
        "date": expense.date,
        "amount": expense.amount,
        "memo": expense.memo,
        "card_id": expense.card_id,
        "category_id": expense.category_id,
        "user_id": expense.user_id,
        "card_name": card.name if card else None,
        "category_name": cat.name if cat else None,
        "user_name": user.name if user else None,
        "created_at": expense.created_at,
    }
