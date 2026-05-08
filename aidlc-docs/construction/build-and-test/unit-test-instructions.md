# Unit Test Instructions

## Backend Tests

```bash
cd backend
pip install -r requirements.txt  # pytest, httpx 포함
pytest tests/ -v
```

### 테스트 구성
| File | Coverage |
|------|----------|
| `tests/test_expenses.py` | 소비 내역 CRUD, 필터링, 유효성 검증 |
| `tests/test_statistics.py` | 월별/연간 통계 조회, 빈 데이터 처리 |

### 테스트 DB
- SQLite in-memory 사용 (conftest.py에서 설정)
- 각 테스트마다 DB 초기화 (autouse fixture)

---

## Frontend Tests (추가 시)

```bash
cd frontend
npm install
npm run test  # vitest 설정 필요 시 추가
```

현재 Frontend는 E2E 테스트로 검증 권장 (통합 테스트 참조).
