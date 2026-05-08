# Business Logic Model - Backend

## API Endpoints

### Expenses
| Method | Path | Description | Response |
|--------|------|-------------|----------|
| POST | /api/expenses | 소비 등록 | 201 Created |
| GET | /api/expenses?year=&month=&category_id=&card_id=&user_id= | 월별 조회 (필터) | 200 OK |
| PUT | /api/expenses/{id} | 소비 수정 | 200 OK |
| DELETE | /api/expenses/{id} | 소비 삭제 | 204 No Content |

### Cards
| Method | Path | Description | Response |
|--------|------|-------------|----------|
| POST | /api/cards | 카드 등록 | 201 Created |
| GET | /api/cards | 카드 목록 | 200 OK |
| PUT | /api/cards/{id} | 카드 수정 | 200 OK |
| DELETE | /api/cards/{id} | 카드 삭제 | 204 No Content |

### Categories
| Method | Path | Description | Response |
|--------|------|-------------|----------|
| POST | /api/categories | 카테고리 등록 | 201 Created |
| GET | /api/categories | 카테고리 목록 | 200 OK |
| PUT | /api/categories/{id} | 카테고리 수정 | 200 OK |
| DELETE | /api/categories/{id} | 카테고리 삭제 | 204 No Content |

### Users
| Method | Path | Description | Response |
|--------|------|-------------|----------|
| POST | /api/users | 사용자 등록 | 201 Created |
| GET | /api/users | 사용자 목록 | 200 OK |
| PUT | /api/users/{id} | 사용자 수정 | 200 OK |
| DELETE | /api/users/{id} | 사용자 삭제 | 204 No Content |

### Statistics
| Method | Path | Description | Response |
|--------|------|-------------|----------|
| GET | /api/statistics/monthly?year=&month= | 월별 통계 | 200 OK |
| GET | /api/statistics/yearly?year= | 연간 통계 | 200 OK |

---

## Statistics Response Models

### MonthlyStats
```json
{
  "year": 2026,
  "month": 5,
  "total": 1500000,
  "prev_month_total": 1300000,
  "diff_total": 200000,
  "diff_rate": 15.38,
  "by_category": [
    { "category_id": 1, "category_name": "식비", "amount": 500000, "rate": 33.3, "prev_amount": 450000, "diff": 50000, "diff_rate": 11.1 }
  ],
  "by_card": [
    { "card_id": 1, "card_name": "신한카드", "amount": 800000, "rate": 53.3 }
  ],
  "by_user": [
    { "user_id": 1, "user_name": "김지영", "amount": 900000, "rate": 60.0 }
  ]
}
```

### YearlyStats
```json
{
  "year": 2026,
  "total": 18000000,
  "prev_year_total": 16000000,
  "diff_total": 2000000,
  "diff_rate": 12.5,
  "monthly": [
    { "month": 1, "total": 1500000 },
    { "month": 2, "total": 1400000 }
  ],
  "by_category": [
    { "category_id": 1, "category_name": "식비", "total": 6000000, "prev_year_total": 5500000, "diff": 500000, "diff_rate": 9.1, "monthly": [{"month": 1, "amount": 500000}] }
  ],
  "by_card": [
    { "card_id": 1, "card_name": "신한카드", "total": 9600000, "monthly": [{"month": 1, "amount": 800000}] }
  ],
  "by_user": [
    { "user_id": 1, "user_name": "김지영", "total": 10800000, "monthly": [{"month": 1, "amount": 900000}] }
  ]
}
```

---

## Service Logic

### StatisticsService.get_monthly_stats(year, month)
1. 해당 월 expense를 조회
2. 총액 합산
3. 카테고리별 GROUP BY → amount, rate 계산
4. 카드별 GROUP BY → amount, rate 계산
5. 사용자별 GROUP BY → amount, rate 계산
6. 전월(year, month-1) 총액 조회 → diff 계산
7. 전월 카테고리별 금액 조회 → 카테고리별 diff 계산
8. 전월 데이터 없으면 diff 필드 = null

### StatisticsService.get_yearly_stats(year)
1. 해당 연도 expense를 월별 GROUP BY → monthly 배열
2. 총액 합산
3. 카테고리별 연간 합계 + 월별 배열
4. 카드별 연간 합계 + 월별 배열
5. 사용자별 연간 합계 + 월별 배열
6. 전년(year-1) 총액 조회 → diff 계산
7. 전년 카테고리별 총액 조회 → 카테고리별 diff 계산
8. 전년 데이터 없으면 diff 필드 = null

### CategoryService.delete(id)
1. "기타" 카테고리인지 확인 → 맞으면 400 에러
2. "기타" 카테고리 ID 조회
3. 해당 카테고리의 expense.category_id를 "기타" ID로 일괄 변경
4. 카테고리 삭제

### CardService.delete(id) / UserService.delete(id)
1. 해당 카드/사용자의 expense FK를 NULL로 일괄 변경
2. 카드/사용자 삭제
