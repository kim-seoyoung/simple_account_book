from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


# --- Card ---
class CardCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CardUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CardOut(BaseModel):
    id: int
    name: str
    created_at: datetime

    model_config = {"from_attributes": True}


# --- Category ---
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CategoryUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CategoryOut(BaseModel):
    id: int
    name: str
    is_default: bool
    created_at: datetime

    model_config = {"from_attributes": True}


# --- User ---
class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class UserUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class UserOut(BaseModel):
    id: int
    name: str
    created_at: datetime

    model_config = {"from_attributes": True}


# --- Expense ---
class ExpenseCreate(BaseModel):
    date: date
    amount: int = Field(..., gt=0)
    memo: Optional[str] = None
    card_id: Optional[int] = None
    category_id: Optional[int] = None
    user_id: Optional[int] = None


class ExpenseUpdate(BaseModel):
    date: Optional[date] = None
    amount: Optional[int] = Field(None, gt=0)
    memo: Optional[str] = None
    card_id: Optional[int] = None
    category_id: Optional[int] = None
    user_id: Optional[int] = None


class ExpenseOut(BaseModel):
    id: int
    date: date
    amount: int
    memo: Optional[str]
    card_id: Optional[int]
    category_id: Optional[int]
    user_id: Optional[int]
    card_name: Optional[str] = None
    category_name: Optional[str] = None
    user_name: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


# --- Statistics ---
class CategoryStat(BaseModel):
    category_id: Optional[int]
    category_name: str
    amount: int
    rate: float
    prev_amount: Optional[int] = None
    diff: Optional[int] = None
    diff_rate: Optional[float] = None


class CardStat(BaseModel):
    card_id: Optional[int]
    card_name: str
    amount: int
    rate: float


class UserStat(BaseModel):
    user_id: Optional[int]
    user_name: str
    amount: int
    rate: float


class MonthlyStats(BaseModel):
    year: int
    month: int
    total: int
    prev_month_total: Optional[int] = None
    diff_total: Optional[int] = None
    diff_rate: Optional[float] = None
    by_category: list[CategoryStat]
    by_card: list[CardStat]
    by_user: list[UserStat]


class MonthlyAmount(BaseModel):
    month: int
    amount: int


class YearlyCategoryStat(BaseModel):
    category_id: Optional[int]
    category_name: str
    total: int
    prev_year_total: Optional[int] = None
    diff: Optional[int] = None
    diff_rate: Optional[float] = None
    monthly: list[MonthlyAmount]


class YearlyCardStat(BaseModel):
    card_id: Optional[int]
    card_name: str
    total: int
    monthly: list[MonthlyAmount]


class YearlyUserStat(BaseModel):
    user_id: Optional[int]
    user_name: str
    total: int
    monthly: list[MonthlyAmount]


class YearlyStats(BaseModel):
    year: int
    total: int
    prev_year_total: Optional[int] = None
    diff_total: Optional[int] = None
    diff_rate: Optional[float] = None
    monthly: list[MonthlyAmount]
    by_category: list[YearlyCategoryStat]
    by_card: list[YearlyCardStat]
    by_user: list[YearlyUserStat]
