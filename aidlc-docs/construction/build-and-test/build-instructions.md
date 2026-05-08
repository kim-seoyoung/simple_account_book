# Build Instructions

## Prerequisites
- Docker & Docker Compose 설치
- (로컬 개발 시) Python 3.12+, Node.js 20+

---

## 전체 서비스 실행 (Docker Compose)

```bash
# 프로젝트 루트에서 실행
docker compose up --build
```

서비스 접근:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **MySQL**: localhost:3306

종료:
```bash
docker compose down
```

데이터 초기화 (볼륨 삭제):
```bash
docker compose down -v
```

---

## 로컬 개발 (Docker 없이)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt

# MySQL 실행 필요 (로컬 또는 Docker)
docker run -d --name mysql-dev -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=account_book -p 3306:3306 mysql:8.0

# 서버 실행
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
