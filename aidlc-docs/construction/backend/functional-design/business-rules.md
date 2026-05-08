# Business Rules - Backend

## Expense Rules

| Rule ID | Rule | Action |
|---------|------|--------|
| EXP-01 | date는 필수 | 400 Bad Request |
| EXP-02 | amount는 필수, 양의 정수 | 400 Bad Request |
| EXP-03 | card_id 입력 시 존재하는 카드여야 함 | 400 Bad Request |
| EXP-04 | category_id 입력 시 존재하는 카테고리여야 함 | 400 Bad Request |
| EXP-05 | user_id 입력 시 존재하는 사용자여야 함 | 400 Bad Request |
| EXP-06 | 존재하지 않는 expense 수정/삭제 시 | 404 Not Found |

## Card Rules

| Rule ID | Rule | Action |
|---------|------|--------|
| CRD-01 | name은 필수, 빈 문자열 불가 | 400 Bad Request |
| CRD-02 | name은 UNIQUE | 409 Conflict |
| CRD-03 | 삭제 시 관련 expense.card_id = NULL | Cascade update |

## Category Rules

| Rule ID | Rule | Action |
|---------|------|--------|
| CAT-01 | name은 필수, 빈 문자열 불가 | 400 Bad Request |
| CAT-02 | name은 UNIQUE | 409 Conflict |
| CAT-03 | 삭제 시 관련 expense.category_id = "기타" 카테고리 ID | Cascade update |
| CAT-04 | "기타" 카테고리는 삭제 불가 | 400 Bad Request |
| CAT-05 | 앱 초기화 시 기본 카테고리 8개 시딩 | 식비, 교통, 쇼핑, 주거, 통신, 의료, 여가, 기타 |

## User Rules

| Rule ID | Rule | Action |
|---------|------|--------|
| USR-01 | name은 필수, 빈 문자열 불가 | 400 Bad Request |
| USR-02 | name은 UNIQUE | 409 Conflict |
| USR-03 | 삭제 시 관련 expense.user_id = NULL | Cascade update |

## Statistics Rules

| Rule ID | Rule | Action |
|---------|------|--------|
| STA-01 | 월별 통계: year, month 필수 | 400 Bad Request |
| STA-02 | 연간 통계: year 필수 | 400 Bad Request |
| STA-03 | 데이터 없는 월/연도 조회 시 빈 결과 반환 (에러 아님) | 200 OK (empty) |
| STA-04 | 전월 대비: 전월 데이터 없으면 증감 = null | 비교 불가 표시 |
| STA-05 | 전년 대비: 전년 데이터 없으면 증감 = null | 비교 불가 표시 |
| STA-06 | 카테고리별 증감: 각 카테고리의 전월/전년 금액 차이 계산 | 카테고리별 diff |
