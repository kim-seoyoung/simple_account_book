# Integration Test Instructions

## 전체 스택 통합 테스트

### 1. 서비스 기동
```bash
docker compose up --build -d
# 모든 서비스 healthy 상태 확인
docker compose ps
```

### 2. API 통합 테스트 (curl)

```bash
# 카테고리 목록 (기본 시딩 확인)
curl http://localhost:8000/api/categories

# 카드 등록
curl -X POST http://localhost:8000/api/cards -H "Content-Type: application/json" -d '{"name":"신한카드"}'

# 소비 등록
curl -X POST http://localhost:8000/api/expenses -H "Content-Type: application/json" -d '{"date":"2026-05-07","amount":15000,"card_id":1,"category_id":1}'

# 월별 조회
curl "http://localhost:8000/api/expenses?year=2026&month=5"

# 월별 통계
curl "http://localhost:8000/api/statistics/monthly?year=2026&month=5"

# 연간 통계
curl "http://localhost:8000/api/statistics/yearly?year=2026"
```

### 3. Frontend 통합 확인
1. http://localhost:5173 접속
2. 설정 탭 → 카드/사용자 추가
3. 소비기록 탭 → 내역 등록/수정/삭제
4. 통계 탭 → 월별/연간 차트 확인

### 4. 정리
```bash
docker compose down -v
```
