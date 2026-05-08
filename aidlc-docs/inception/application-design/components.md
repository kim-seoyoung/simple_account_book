# Components

## Backend Components

### 1. Expense API
- **Purpose**: 소비 내역 CRUD REST API
- **Responsibilities**:
  - 소비 내역 등록/조회/수정/삭제 엔드포인트 제공
  - 월별 필터링, 카테고리/카드/사용자별 필터링
  - 입력 검증 (필수 필드, 금액 양수)

### 2. Card API
- **Purpose**: 카드 관리 REST API
- **Responsibilities**:
  - 카드 CRUD 엔드포인트 제공
  - 카드 삭제 시 관련 소비 내역 업데이트

### 3. Category API
- **Purpose**: 카테고리 관리 REST API
- **Responsibilities**:
  - 카테고리 CRUD 엔드포인트 제공
  - 기본 카테고리 시딩
  - 카테고리 삭제 시 관련 소비 내역 "기타"로 변경

### 4. User Label API
- **Purpose**: 사용자(라벨) 관리 REST API
- **Responsibilities**:
  - 사용자 CRUD 엔드포인트 제공
  - 사용자 삭제 시 관련 소비 내역 업데이트

### 5. Statistics API
- **Purpose**: 월별/연간 통계 조회 REST API
- **Responsibilities**:
  - 월별 통계 (카테고리별/카드별/사용자별 합계 및 비율)
  - 연간 통계 (월별 추이, 전년 대비)
  - 전월 대비 증감 계산 (총액 + 카테고리별)
  - 전년 대비 증감 계산 (총액 + 카테고리별)

### 6. Database Layer
- **Purpose**: MySQL 데이터 접근 계층
- **Responsibilities**:
  - SQLAlchemy ORM 모델 정의
  - DB 세션 관리
  - 마이그레이션 (Alembic)

---

## Frontend Components

### 7. Expense View
- **Purpose**: 소비 내역 등록/조회/수정/삭제 화면
- **Responsibilities**:
  - 소비 등록 폼
  - 월별 내역 목록 (필터링, 정렬)
  - 수정/삭제 UI

### 8. Settings View
- **Purpose**: 카드/카테고리/사용자 관리 화면
- **Responsibilities**:
  - 카드 목록 및 CRUD
  - 카테고리 목록 및 CRUD
  - 사용자 목록 및 CRUD

### 9. Statistics View
- **Purpose**: 월별/연간 통계 차트 화면
- **Responsibilities**:
  - 월별 통계 차트 (파이/바)
  - 연간 추이 차트 (라인/바)
  - 전월/전년 대비 표시

### 10. API Client
- **Purpose**: 백엔드 API 통신 모듈
- **Responsibilities**:
  - Axios 기반 HTTP 클라이언트
  - API 엔드포인트 호출 래핑
  - 에러 핸들링
