# Unit of Work

## Unit 1: Backend + DB

| 항목 | 내용 |
|------|------|
| Name | backend |
| Type | Service (독립 배포 가능) |
| Tech | Python, FastAPI, SQLAlchemy, Alembic, MySQL |
| Purpose | REST API 서버 + 데이터베이스 스키마/마이그레이션 |

**Responsibilities**:
- 소비 내역 CRUD API
- 카드/카테고리/사용자 관리 API
- 월별/연간 통계 집계 API (카테고리별 증감 포함)
- DB 스키마 정의 및 마이그레이션
- 입력 검증 및 비즈니스 로직

**Code Organization**:
```
backend/
├── app/
│   ├── main.py              # FastAPI app entry
│   ├── database.py          # DB connection, session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── routers/
│   │   ├── expenses.py
│   │   ├── cards.py
│   │   ├── categories.py
│   │   ├── users.py
│   │   └── statistics.py
│   └── services/
│       ├── expense_service.py
│       ├── card_service.py
│       ├── category_service.py
│       ├── user_service.py
│       └── statistics_service.py
├── alembic/                 # DB migrations
├── requirements.txt
├── Dockerfile
└── tests/
```

---

## Unit 2: Frontend

| 항목 | 내용 |
|------|------|
| Name | frontend |
| Type | Service (독립 배포 가능) |
| Tech | Vue.js 3, Vue Router, Pinia, Chart.js, Axios |
| Purpose | 웹 UI (소비 기록, 설정, 통계 차트) |

**Responsibilities**:
- 소비 내역 등록/조회/수정/삭제 화면
- 카드/카테고리/사용자 설정 화면
- 월별/연간 통계 차트 화면
- Backend API 연동

**Code Organization**:
```
frontend/
├── src/
│   ├── main.js
│   ├── App.vue
│   ├── router/
│   │   └── index.js
│   ├── stores/
│   │   └── app.js           # Pinia store
│   ├── api/
│   │   └── index.js         # Axios API client
│   ├── views/
│   │   ├── ExpenseView.vue
│   │   ├── StatisticsView.vue
│   │   └── SettingsView.vue
│   └── components/
│       ├── ExpenseForm.vue
│       ├── ExpenseList.vue
│       ├── MonthlyChart.vue
│       ├── YearlyChart.vue
│       └── ...
├── package.json
├── Dockerfile
└── vite.config.js
```

---

## Execution Order
**Unit 1 (Backend+DB) → Unit 2 (Frontend)**

이유: Frontend가 Backend API에 의존하므로 API를 먼저 구현하여 Frontend 개발 시 실제 API 연동 가능.

## Docker Compose (전체 통합)
```
docker-compose.yml          # 루트에 위치
├── backend (port 8000)
├── frontend (port 5173)
└── mysql (port 3306)
```
