# Code Summary - Frontend

## Generated Files

| Path | Purpose |
|------|---------|
| `frontend/package.json` | 의존성 정의 |
| `frontend/vite.config.js` | Vite 설정 |
| `frontend/Dockerfile` | Docker 이미지 빌드 |
| `frontend/index.html` | HTML 엔트리 |
| `frontend/src/main.js` | Vue 앱 초기화 |
| `frontend/src/App.vue` | 루트 컴포넌트 + 네비게이션 |
| `frontend/src/router/index.js` | 라우팅 설정 |
| `frontend/src/api/index.js` | Axios API 클라이언트 |
| `frontend/src/stores/app.js` | Pinia 전역 스토어 |
| `frontend/src/views/ExpenseView.vue` | 소비 내역 화면 |
| `frontend/src/views/StatisticsView.vue` | 통계 화면 |
| `frontend/src/views/SettingsView.vue` | 설정 화면 |
| `frontend/src/components/ExpenseForm.vue` | 소비 등록/수정 폼 |
| `frontend/src/components/ExpenseList.vue` | 소비 내역 목록 |
| `frontend/src/components/MonthlyChart.vue` | 월별 통계 차트 |
| `frontend/src/components/YearlyChart.vue` | 연간 통계 차트 |
| `docker-compose.yml` | 전체 서비스 통합 실행 |

## Routes
- `/` — 소비 기록 (기본)
- `/statistics` — 월별/연간 통계
- `/settings` — 카드/카테고리/사용자 관리
