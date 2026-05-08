# Code Generation Plan - Backend+DB

## Unit Context
- **Unit**: Backend + DB
- **Tech**: Python, FastAPI, SQLAlchemy, Alembic, MySQL
- **Location**: `backend/` (workspace root)
- **Stories**: US-1.1~1.3, US-2.1~2.4, US-3.1~3.2 (API + DB 부분)

## Generation Steps

### Step 1: Project Structure Setup
- [x] `backend/requirements.txt` — 의존성 정의
- [x] `backend/Dockerfile` — Docker 이미지 빌드
- [x] `backend/app/__init__.py`
- [x] `backend/app/main.py` — FastAPI 앱 엔트리포인트

### Step 2: Database Layer
- [x] `backend/app/database.py` — DB 연결, 세션 관리
- [x] `backend/app/models.py` — SQLAlchemy 모델 (Expense, Card, Category, User)
- [x] `backend/app/schemas.py` — Pydantic 스키마 (요청/응답 모델)

### Step 3: Category Router & Service (US-1.1)
- [x] `backend/app/services/category_service.py`
- [x] `backend/app/routers/categories.py`

### Step 4: Card Router & Service (US-1.2)
- [x] `backend/app/services/card_service.py`
- [x] `backend/app/routers/cards.py`

### Step 5: User Router & Service (US-1.3)
- [x] `backend/app/services/user_service.py`
- [x] `backend/app/routers/users.py`

### Step 6: Expense Router & Service (US-2.1~2.4)
- [x] `backend/app/services/expense_service.py`
- [x] `backend/app/routers/expenses.py`

### Step 7: Statistics Router & Service (US-3.1~3.2)
- [x] `backend/app/services/statistics_service.py`
- [x] `backend/app/routers/statistics.py`

### Step 8: DB Initialization (Seed)
- [x] `backend/app/init_db.py` — 기본 카테고리 시딩, 테이블 생성

### Step 9: Tests
- [x] `backend/tests/__init__.py`
- [x] `backend/tests/test_expenses.py`
- [x] `backend/tests/test_statistics.py`

### Step 10: Documentation
- [x] `aidlc-docs/construction/backend/code/code-summary.md`
