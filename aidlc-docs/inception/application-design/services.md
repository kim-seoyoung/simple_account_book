# Services

## Backend Services

### ExpenseService
- **Purpose**: 소비 내역 비즈니스 로직 처리
- **Orchestration**:
  - 소비 등록 시 필수 필드 검증, FK 유효성 확인
  - 조회 시 월별 필터링 + 카테고리/카드/사용자 필터 조합
  - 삭제 시 확인 후 DB 삭제

### CardService
- **Purpose**: 카드 관리 비즈니스 로직
- **Orchestration**:
  - 카드 삭제 시 관련 expense의 card_id를 NULL로 업데이트

### CategoryService
- **Purpose**: 카테고리 관리 비즈니스 로직
- **Orchestration**:
  - 카테고리 삭제 시 관련 expense의 category_id를 "기타" 카테고리 ID로 변경
  - 앱 초기화 시 기본 카테고리 시딩

### UserLabelService
- **Purpose**: 사용자 라벨 관리 비즈니스 로직
- **Orchestration**:
  - 사용자 삭제 시 관련 expense의 user_id를 NULL로 업데이트

### StatisticsService
- **Purpose**: 통계 집계 로직
- **Orchestration**:
  - 월별: 해당 월 expense를 카테고리/카드/사용자별 GROUP BY 집계
  - 월별: 전월 대비 총액 증감 + 카테고리별 증감 계산
  - 연간: 해당 연도 12개월 월별 합계 집계
  - 연간: 전년 대비 총액 증감 + 카테고리별 연간 증감 계산

---

## Frontend Services

### Vue Router
- **Purpose**: 페이지 라우팅
- **Routes**: / (소비 내역) | /statistics (통계) | /settings (설정)

### Pinia Store (선택)
- **Purpose**: 전역 상태 관리 (카드/카테고리/사용자 목록 캐싱)
- **Orchestration**: 앱 로드 시 카드/카테고리/사용자 목록 fetch 후 캐싱
