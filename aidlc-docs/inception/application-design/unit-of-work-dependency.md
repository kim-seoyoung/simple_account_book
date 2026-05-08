# Unit of Work Dependencies

## Dependency Matrix

| From | To | Type | Description |
|------|----|------|-------------|
| Frontend | Backend | Runtime | HTTP REST API 호출 |
| Backend | MySQL | Runtime | DB 접근 (SQLAlchemy ORM) |
| Frontend | MySQL | None | 직접 의존 없음 |

## Dependency Diagram

```
+------------+       HTTP/JSON       +------------+       ORM        +-------+
|  Frontend  |  ─────────────────>   |  Backend   |  ────────────>   | MySQL |
|  (Vue.js)  |                       |  (FastAPI) |                  |       |
+------------+                       +------------+                  +-------+
```

## Integration Points

| Interface | Protocol | Format | Notes |
|-----------|----------|--------|-------|
| Backend REST API | HTTP | JSON | Frontend → Backend 통신 |
| Database | TCP/3306 | MySQL protocol | Backend → MySQL |

## Build/Deploy Dependencies
- **Frontend**: Backend API URL 환경변수 필요 (VITE_API_URL)
- **Backend**: MySQL 연결 정보 환경변수 필요 (DATABASE_URL)
- **MySQL**: 독립적, 의존성 없음

## Execution Constraints
- MySQL이 먼저 기동되어야 Backend 시작 가능
- Backend가 기동되어야 Frontend가 정상 동작
- Docker Compose의 depends_on으로 순서 보장
