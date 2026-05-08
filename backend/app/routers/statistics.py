from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import MonthlyStats, YearlyStats
from app.services import statistics_service

router = APIRouter()


@router.get("/monthly", response_model=MonthlyStats)
def monthly(year: int = Query(...), month: int = Query(...), db: Session = Depends(get_db)):
    return statistics_service.get_monthly_stats(db, year, month)


@router.get("/yearly", response_model=YearlyStats)
def yearly(year: int = Query(...), db: Session = Depends(get_db)):
    return statistics_service.get_yearly_stats(db, year)
