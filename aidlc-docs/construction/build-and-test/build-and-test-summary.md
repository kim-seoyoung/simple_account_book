# Build and Test Summary

## Quick Start
```bash
docker compose up --build
```
- Frontend: http://localhost:5173
- Backend: http://localhost:8000/docs

## Test Commands
| Type | Command | Location |
|------|---------|----------|
| Backend Unit Tests | `pytest tests/ -v` | `backend/` |
| Full Stack | `docker compose up --build` | project root |

## Verification Checklist
- [ ] `docker compose up --build` 성공
- [ ] http://localhost:8000/docs 접근 가능 (Swagger UI)
- [ ] http://localhost:5173 접근 가능 (Vue 앱)
- [ ] 기본 카테고리 8개 시딩 확인 (GET /api/categories)
- [ ] 소비 내역 등록/조회/수정/삭제 동작
- [ ] 카드/카테고리/사용자 CRUD 동작
- [ ] 월별 통계 차트 표시
- [ ] 연간 통계 차트 표시
- [ ] 카테고리별 전월/전년 대비 증감 표시
- [ ] 필터링 (카테고리/카드/사용자) 동작
