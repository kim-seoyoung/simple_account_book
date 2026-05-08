# Code Summary - Backend+DB

## Generated Files

| Path | Purpose |
|------|---------|
| `backend/requirements.txt` | Python 의존성 |
| `backend/Dockerfile` | Docker 이미지 빌드 |
| `backend/app/main.py` | FastAPI 앱 엔트리포인트 |
| `backend/app/database.py` | DB 연결, 세션 관리 |
| `backend/app/models.py` | SQLAlchemy 모델 (4 entities) |
| `backend/app/schemas.py` | Pydantic 요청/응답 스키마 |
| `backend/app/init_db.py` | 기본 카테고리 시딩 |
| `backend/app/services/category_service.py` | 카테고리 비즈니스 로직 |
| `backend/app/services/card_service.py` | 카드 비즈니스 로직 |
| `backend/app/services/user_service.py` | 사용자 비즈니스 로직 |
| `backend/app/services/expense_service.py` | 소비 내역 비즈니스 로직 |
| `backend/app/services/statistics_service.py` | 통계 집계 로직 |
| `backend/app/routers/categories.py` | 카테고리 API 라우터 |
| `backend/app/routers/cards.py` | 카드 API 라우터 |
| `backend/app/routers/users.py` | 사용자 API 라우터 |
| `backend/app/routers/expenses.py` | 소비 내역 API 라우터 |
| `backend/app/routers/statistics.py` | 통계 API 라우터 |
| `backend/tests/conftest.py` | 테스트 설정 (SQLite in-memory) |
| `backend/tests/test_expenses.py` | 소비 내역 API 테스트 |
| `backend/tests/test_statistics.py` | 통계 API 테스트 |

## API Endpoints (14)
- POST/GET/PUT/DELETE `/api/expenses`
- POST/GET/PUT/DELETE `/api/cards`
- POST/GET/PUT/DELETE `/api/categories`
- POST/GET/PUT/DELETE `/api/users`
- GET `/api/statistics/monthly`
- GET `/api/statistics/yearly`
