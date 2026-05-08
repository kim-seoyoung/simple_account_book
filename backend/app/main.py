from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.init_db import seed_categories
from app.routers import expenses, cards, categories, users, statistics


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_categories()
    yield


app = FastAPI(title="가계부 API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expenses.router, prefix="/api/expenses", tags=["expenses"])
app.include_router(cards.router, prefix="/api/cards", tags=["cards"])
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(statistics.router, prefix="/api/statistics", tags=["statistics"])
