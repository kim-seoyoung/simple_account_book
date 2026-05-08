from app.database import SessionLocal
from app.models import Category

DEFAULT_CATEGORIES = ["식비", "교통", "쇼핑", "주거", "통신", "의료", "여가", "기타"]


def seed_categories():
    db = SessionLocal()
    try:
        if db.query(Category).count() == 0:
            for name in DEFAULT_CATEGORIES:
                db.add(Category(name=name, is_default=True))
            db.commit()
    finally:
        db.close()
