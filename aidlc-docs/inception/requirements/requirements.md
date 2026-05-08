# 가계부 서비스 요구사항

## Intent Analysis
- **User Request**: 가정 소비 금액을 카드별, 카테고리별, 사용자별로 월 단위 기록하고 월별/연간 통계를 확인하는 가계부 웹 서비스
- **Request Type**: New Project (Greenfield)
- **Scope Estimate**: Multiple Components (프론트엔드 + 백엔드 + DB)
- **Complexity Estimate**: Moderate

---

## 기술 스택

| 구분 | 선택 |
|------|------|
| Frontend | Vue.js |
| Backend | Python (FastAPI) |
| Database | MySQL |
| Chart Library | Chart.js (Vue.js 호환, 경량) |
| Container | Docker + Docker Compose |
| Authentication | 없음 (사용자는 단순 라벨) |

---

## Functional Requirements

### FR-1: 소비 내역 관리
- **FR-1.1**: 소비 내역 등록 (날짜, 금액, 사용자, 카드, 카테고리, 메모)
- **FR-1.2**: 월 단위 소비 내역 목록 조회
- **FR-1.3**: 카테고리별/카드별/사용자별 필터링
- **FR-1.4**: 소비 내역 수정
- **FR-1.5**: 소비 내역 삭제 (확인 팝업)
- **FR-1.6**: 날짜순 정렬 (최신순 기본)
- **FR-1.7**: 필수 필드 검증 (날짜, 금액), 금액은 양수만 허용

### FR-2: 카드 관리
- **FR-2.1**: 카드 이름 등록
- **FR-2.2**: 카드 목록 조회
- **FR-2.3**: 카드 수정/삭제
- **FR-2.4**: 삭제 시 관련 소비 내역은 "카드 없음"으로 변경

### FR-3: 카테고리 관리
- **FR-3.1**: 카테고리 이름 등록
- **FR-3.2**: 기본 카테고리 제공 (식비, 교통, 쇼핑, 주거, 통신, 의료, 여가, 기타)
- **FR-3.3**: 카테고리 추가/수정/삭제
- **FR-3.4**: 삭제 시 관련 소비 내역은 "기타"로 변경

### FR-4: 사용자 관리
- **FR-4.1**: 사용자 이름 등록
- **FR-4.2**: 사용자 목록 조회
- **FR-4.3**: 사용자 수정/삭제
- **FR-4.4**: 삭제 시 관련 소비 내역은 "사용자 없음"으로 변경

### FR-5: 월별 통계
- **FR-5.1**: 월 선택 기능
- **FR-5.2**: 카테고리별 총 소비 금액 및 비율 (파이/바 차트)
- **FR-5.3**: 카드별 총 소비 금액 및 비율
- **FR-5.4**: 사용자별 총 소비 금액 및 비율
- **FR-5.5**: 월 총계 표시
- **FR-5.6**: 전월 대비 증감액 및 증감률 (총액 + 카테고리별)

### FR-6: 연간 통계
- **FR-6.1**: 연도 선택 기능
- **FR-6.2**: 1~12월 월별 총 소비 금액 추이 (라인/바 차트)
- **FR-6.3**: 카테고리별 월별 소비 추이
- **FR-6.4**: 카드별 월별 소비 추이
- **FR-6.5**: 사용자별 월별 소비 추이
- **FR-6.6**: 연간 총계
- **FR-6.7**: 전년 대비 증감률 (총액 + 카테고리별)

---

## Non-Functional Requirements

### NFR-1: 배포
- Docker Compose로 프론트엔드, 백엔드, MySQL을 한 번에 실행
- 로컬 개발 환경에서도 동일하게 동작

### NFR-2: 성능
- API 응답 시간 500ms 이내 (일반 CRUD)
- 통계 조회 1초 이내

### NFR-3: 사용성
- 반응형 웹 디자인 (모바일/데스크톱)
- 직관적인 UI (최소 클릭으로 소비 등록)

---

## Constraints (제외 사항)
- 실제 결제/PG 연동 없음
- 복잡한 인증(OAuth, 2FA) 없음
- 푸시/SMS/이메일 알림 없음
- 외부 시스템 연동 없음

---

## Extension Configuration

| Extension | Enabled | Decided At |
|---|---|---|
| Property-Based Testing | Partial (순수 함수, 직렬화만) | Requirements Analysis |
| Security Baseline | No | Requirements Analysis |
