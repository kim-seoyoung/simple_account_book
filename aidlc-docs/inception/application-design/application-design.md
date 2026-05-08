# Application Design

## Overview
가계부 웹 서비스의 애플리케이션 아키텍처. 프론트엔드(Vue.js)와 백엔드(FastAPI+MySQL)로 분리된 2-tier 웹 애플리케이션.

## Architecture

```
+-------------------+       +-------------------+       +----------+
|   Vue.js Frontend |  -->  |  FastAPI Backend   |  -->  |  MySQL   |
|   (Port 5173)     |  HTTP |  (Port 8000)       |  ORM  |  (3306)  |
+-------------------+       +-------------------+       +----------+
| - Expense View    |       | - Expense API      |       | expenses |
| - Statistics View |       | - Card API         |       | cards    |
| - Settings View   |       | - Category API     |       | categories|
| - API Client      |       | - User Label API   |       | users    |
|                   |       | - Statistics API   |       |          |
+-------------------+       +-------------------+       +----------+
```

## Tech Stack
- **Frontend**: Vue.js 3 + Vue Router + Pinia + Chart.js + Axios
- **Backend**: Python + FastAPI + SQLAlchemy + Alembic
- **Database**: MySQL 8
- **Container**: Docker Compose (frontend + backend + mysql)

## Key Design Decisions
1. **REST API**: 프론트-백 간 JSON REST 통신
2. **ORM**: SQLAlchemy로 DB 접근, Alembic으로 마이그레이션
3. **No Auth**: 인증 없음, 사용자는 단순 라벨
4. **Stateless Backend**: 세션 없음, 모든 상태는 DB에 저장
5. **Docker Compose**: 개발/배포 환경 통일

## Detailed Artifacts
- [components.md](components.md) — 컴포넌트 정의
- [component-methods.md](component-methods.md) — 메서드 시그니처
- [services.md](services.md) — 서비스 레이어
- [component-dependency.md](component-dependency.md) — 의존성 관계
