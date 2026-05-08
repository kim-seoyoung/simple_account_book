# Component Dependencies

## Dependency Matrix

```
Frontend          →  Backend API  →  Database
─────────────────────────────────────────────
Expense View      →  Expense API  →  expenses table
Settings View     →  Card API     →  cards table
                  →  Category API →  categories table
                  →  User API     →  users table
Statistics View   →  Statistics API → expenses table (집계)
API Client        →  All APIs
```

## Communication Patterns

| From | To | Pattern | Protocol |
|------|----|---------|----------|
| Frontend (API Client) | Backend APIs | REST HTTP | JSON over HTTP |
| Backend APIs | Services | Direct call | Python function |
| Services | Database Layer | ORM | SQLAlchemy |
| Database Layer | MySQL | TCP | MySQL protocol |

## Data Flow

```
[Vue.js Frontend]
       |
       | HTTP REST (JSON)
       v
[FastAPI Backend]
       |
       | SQLAlchemy ORM
       v
[MySQL Database]
```

## Inter-Component Dependencies

- **Statistics API** depends on: expenses, categories, cards, users 테이블
- **Expense API** depends on: cards, categories, users (FK 참조)
- **Card/Category/User API**: 독립적, 삭제 시 expense 테이블 업데이트
- **Frontend Views**: API Client를 통해 모든 Backend API에 의존
