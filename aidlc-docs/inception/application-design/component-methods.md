# Component Methods

## Backend API Methods

### Expense API
| Method | Endpoint | Input | Output |
|--------|----------|-------|--------|
| create_expense | POST /api/expenses | ExpenseCreate (date, amount, user_id?, card_id?, category_id?, memo?) | Expense |
| list_expenses | GET /api/expenses?year=&month=&category_id=&card_id=&user_id= | Query params | List[Expense] |
| update_expense | PUT /api/expenses/{id} | ExpenseUpdate | Expense |
| delete_expense | DELETE /api/expenses/{id} | Path param | None |

### Card API
| Method | Endpoint | Input | Output |
|--------|----------|-------|--------|
| create_card | POST /api/cards | CardCreate (name) | Card |
| list_cards | GET /api/cards | None | List[Card] |
| update_card | PUT /api/cards/{id} | CardUpdate (name) | Card |
| delete_card | DELETE /api/cards/{id} | Path param | None |

### Category API
| Method | Endpoint | Input | Output |
|--------|----------|-------|--------|
| create_category | POST /api/categories | CategoryCreate (name) | Category |
| list_categories | GET /api/categories | None | List[Category] |
| update_category | PUT /api/categories/{id} | CategoryUpdate (name) | Category |
| delete_category | DELETE /api/categories/{id} | Path param | None |

### User Label API
| Method | Endpoint | Input | Output |
|--------|----------|-------|--------|
| create_user | POST /api/users | UserCreate (name) | User |
| list_users | GET /api/users | None | List[User] |
| update_user | PUT /api/users/{id} | UserUpdate (name) | User |
| delete_user | DELETE /api/users/{id} | Path param | None |

### Statistics API
| Method | Endpoint | Input | Output |
|--------|----------|-------|--------|
| get_monthly_stats | GET /api/statistics/monthly?year=&month= | Query params | MonthlyStats |
| get_yearly_stats | GET /api/statistics/yearly?year= | Query params | YearlyStats |

---

## Frontend Methods (주요 컴포저블/스토어)

### API Client
| Method | Purpose |
|--------|---------|
| api.expenses.list(params) | 소비 내역 목록 조회 |
| api.expenses.create(data) | 소비 내역 등록 |
| api.expenses.update(id, data) | 소비 내역 수정 |
| api.expenses.delete(id) | 소비 내역 삭제 |
| api.cards.list() | 카드 목록 조회 |
| api.cards.create(data) | 카드 등록 |
| api.categories.list() | 카테고리 목록 조회 |
| api.users.list() | 사용자 목록 조회 |
| api.statistics.monthly(year, month) | 월별 통계 조회 |
| api.statistics.yearly(year) | 연간 통계 조회 |

**Note**: 상세 비즈니스 로직 및 검증 규칙은 Functional Design에서 정의
