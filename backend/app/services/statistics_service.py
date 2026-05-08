from sqlalchemy import extract, func
from sqlalchemy.orm import Session

from app.models import Expense, Card, Category, User


def get_monthly_stats(db: Session, year: int, month: int) -> dict:
    expenses = db.query(Expense).filter(
        extract("year", Expense.date) == year,
        extract("month", Expense.date) == month,
    ).all()

    total = sum(e.amount for e in expenses)

    # Previous month
    prev_year, prev_month = (year, month - 1) if month > 1 else (year - 1, 12)
    prev_expenses = db.query(Expense).filter(
        extract("year", Expense.date) == prev_year,
        extract("month", Expense.date) == prev_month,
    ).all()
    prev_total = sum(e.amount for e in prev_expenses) if prev_expenses else None

    # By category
    by_category = _group_by_category(db, expenses, total)
    prev_by_cat = _category_totals(prev_expenses) if prev_expenses else {}
    for cat_stat in by_category:
        prev_amt = prev_by_cat.get(cat_stat["category_id"])
        if prev_amt is not None:
            cat_stat["prev_amount"] = prev_amt
            cat_stat["diff"] = cat_stat["amount"] - prev_amt
            cat_stat["diff_rate"] = round((cat_stat["amount"] - prev_amt) / prev_amt * 100, 2) if prev_amt else None

    # By card
    by_card = _group_by_card(db, expenses, total)

    # By user
    by_user = _group_by_user(db, expenses, total)

    return {
        "year": year,
        "month": month,
        "total": total,
        "prev_month_total": prev_total,
        "diff_total": total - prev_total if prev_total is not None else None,
        "diff_rate": round((total - prev_total) / prev_total * 100, 2) if prev_total else None,
        "by_category": by_category,
        "by_card": by_card,
        "by_user": by_user,
    }


def get_yearly_stats(db: Session, year: int) -> dict:
    expenses = db.query(Expense).filter(extract("year", Expense.date) == year).all()
    total = sum(e.amount for e in expenses)

    # Previous year
    prev_expenses = db.query(Expense).filter(extract("year", Expense.date) == year - 1).all()
    prev_total = sum(e.amount for e in prev_expenses) if prev_expenses else None

    # Monthly totals
    monthly = []
    for m in range(1, 13):
        amt = sum(e.amount for e in expenses if e.date.month == m)
        monthly.append({"month": m, "amount": amt})

    # By category yearly
    cat_map: dict[int | None, list] = {}
    for e in expenses:
        cat_map.setdefault(e.category_id, []).append(e)

    prev_cat_totals = _category_totals(prev_expenses) if prev_expenses else {}

    by_category = []
    for cat_id, cat_expenses in cat_map.items():
        cat = db.query(Category).get(cat_id) if cat_id else None
        cat_total = sum(e.amount for e in cat_expenses)
        cat_monthly = [{"month": m, "amount": sum(e.amount for e in cat_expenses if e.date.month == m)} for m in range(1, 13)]
        prev_cat_total = prev_cat_totals.get(cat_id)
        by_category.append({
            "category_id": cat_id,
            "category_name": cat.name if cat else "카테고리 없음",
            "total": cat_total,
            "prev_year_total": prev_cat_total,
            "diff": cat_total - prev_cat_total if prev_cat_total is not None else None,
            "diff_rate": round((cat_total - prev_cat_total) / prev_cat_total * 100, 2) if prev_cat_total else None,
            "monthly": cat_monthly,
        })

    # By card yearly
    card_map: dict[int | None, list] = {}
    for e in expenses:
        card_map.setdefault(e.card_id, []).append(e)

    by_card = []
    for card_id, card_expenses in card_map.items():
        card = db.query(Card).get(card_id) if card_id else None
        by_card.append({
            "card_id": card_id,
            "card_name": card.name if card else "카드 없음",
            "total": sum(e.amount for e in card_expenses),
            "monthly": [{"month": m, "amount": sum(e.amount for e in card_expenses if e.date.month == m)} for m in range(1, 13)],
        })

    # By user yearly
    user_map: dict[int | None, list] = {}
    for e in expenses:
        user_map.setdefault(e.user_id, []).append(e)

    by_user = []
    for uid, user_expenses in user_map.items():
        user = db.query(User).get(uid) if uid else None
        by_user.append({
            "user_id": uid,
            "user_name": user.name if user else "사용자 없음",
            "total": sum(e.amount for e in user_expenses),
            "monthly": [{"month": m, "amount": sum(e.amount for e in user_expenses if e.date.month == m)} for m in range(1, 13)],
        })

    return {
        "year": year,
        "total": total,
        "prev_year_total": prev_total,
        "diff_total": total - prev_total if prev_total is not None else None,
        "diff_rate": round((total - prev_total) / prev_total * 100, 2) if prev_total else None,
        "monthly": monthly,
        "by_category": by_category,
        "by_card": by_card,
        "by_user": by_user,
    }


def _group_by_category(db: Session, expenses: list, total: int) -> list[dict]:
    cat_map: dict[int | None, int] = {}
    for e in expenses:
        cat_map[e.category_id] = cat_map.get(e.category_id, 0) + e.amount
    result = []
    for cat_id, amount in cat_map.items():
        cat = db.query(Category).get(cat_id) if cat_id else None
        result.append({
            "category_id": cat_id,
            "category_name": cat.name if cat else "카테고리 없음",
            "amount": amount,
            "rate": round(amount / total * 100, 2) if total else 0,
            "prev_amount": None,
            "diff": None,
            "diff_rate": None,
        })
    return result


def _group_by_card(db: Session, expenses: list, total: int) -> list[dict]:
    card_map: dict[int | None, int] = {}
    for e in expenses:
        card_map[e.card_id] = card_map.get(e.card_id, 0) + e.amount
    result = []
    for card_id, amount in card_map.items():
        card = db.query(Card).get(card_id) if card_id else None
        result.append({
            "card_id": card_id,
            "card_name": card.name if card else "카드 없음",
            "amount": amount,
            "rate": round(amount / total * 100, 2) if total else 0,
        })
    return result


def _group_by_user(db: Session, expenses: list, total: int) -> list[dict]:
    user_map: dict[int | None, int] = {}
    for e in expenses:
        user_map[e.user_id] = user_map.get(e.user_id, 0) + e.amount
    result = []
    for uid, amount in user_map.items():
        user = db.query(User).get(uid) if uid else None
        result.append({
            "user_id": uid,
            "user_name": user.name if user else "사용자 없음",
            "amount": amount,
            "rate": round(amount / total * 100, 2) if total else 0,
        })
    return result


def _category_totals(expenses: list) -> dict[int | None, int]:
    totals: dict[int | None, int] = {}
    for e in expenses:
        totals[e.category_id] = totals.get(e.category_id, 0) + e.amount
    return totals
