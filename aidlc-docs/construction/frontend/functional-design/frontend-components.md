# Frontend Components Design

## Route Structure
| Path | View | Description |
|------|------|-------------|
| `/` | ExpenseView | 소비 내역 (기본 화면) |
| `/statistics` | StatisticsView | 월별/연간 통계 |
| `/settings` | SettingsView | 카드/카테고리/사용자 관리 |

---

## Component Hierarchy

```
App.vue
├── NavBar.vue (탭 네비게이션: 소비기록 | 통계 | 설정)
├── ExpenseView.vue
│   ├── MonthSelector.vue
│   ├── ExpenseFilter.vue (카테고리/카드/사용자 필터)
│   ├── ExpenseList.vue
│   │   └── ExpenseItem.vue (개별 항목, 수정/삭제 버튼)
│   ├── ExpenseForm.vue (등록/수정 모달)
│   └── ConfirmDialog.vue (삭제 확인)
├── StatisticsView.vue
│   ├── MonthlyStats.vue
│   │   ├── MonthSelector.vue
│   │   ├── CategoryPieChart.vue
│   │   ├── CardBarChart.vue
│   │   ├── UserBarChart.vue
│   │   └── ComparisonSummary.vue (전월 대비)
│   └── YearlyStats.vue
│       ├── YearSelector.vue
│       ├── MonthlyTrendChart.vue (라인 차트)
│       ├── CategoryTrendChart.vue
│       └── YearComparisonSummary.vue (전년 대비)
└── SettingsView.vue
    ├── CardManager.vue (CRUD 리스트)
    ├── CategoryManager.vue (CRUD 리스트)
    ├── UserManager.vue (CRUD 리스트)
    └── ConfirmDialog.vue (삭제 확인)
```

---

## State Management (Pinia)

### appStore
| State | Type | Purpose |
|-------|------|---------|
| cards | Card[] | 카드 목록 캐시 |
| categories | Category[] | 카테고리 목록 캐시 |
| users | User[] | 사용자 목록 캐시 |

**Actions**: fetchCards(), fetchCategories(), fetchUsers() — 앱 로드 시 호출

---

## Key Interactions

### 소비 등록 Flow
1. ExpenseView → "+" 버튼 클릭 → ExpenseForm 모달 열림
2. 날짜, 금액 입력 (필수) + 카드/카테고리/사용자/메모 선택
3. 저장 → POST /api/expenses → 목록 새로고침

### 소비 삭제 Flow
1. ExpenseItem → 삭제 버튼 → ConfirmDialog 표시
2. 확인 → DELETE /api/expenses/{id} → 목록 새로고침

### 통계 조회 Flow
1. StatisticsView → 탭 전환 (월별/연간)
2. 월/연도 선택 → GET /api/statistics/monthly 또는 /yearly
3. Chart.js로 차트 렌더링

---

## Form Validation (Frontend)
| Field | Rule |
|-------|------|
| date | 필수, 유효한 날짜 |
| amount | 필수, 양의 정수 |
| name (설정) | 필수, 빈 문자열 불가 |
