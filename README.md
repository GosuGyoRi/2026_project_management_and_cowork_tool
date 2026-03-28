# 2026 프로젝트 관리 & 협업 툴

Flow(flow.team)와 유사한 사내 업무 협업 및 프로젝트 관리 서비스입니다.

## 서비스 구성

| 서비스 | 경로 | 포트 | 담당 |
|--------|------|------|------|
| Backend REST API | `./backend` | 8000 | 개발자 1 |
| Realtime Server (WebSocket) | `./realtime` | 8001 | 개발자 2 |
| Frontend (React) | `./frontend` | 3000 | 개발자 3 |
| AI Chatbot | `./ai-chatbot` | 8002 | 개발자 4 |
| PostgreSQL | - | 5432 | 개발자 3 (DB 관리) |
| Redis | - | 6379 | - |

## 기술 스택

- **Backend**: FastAPI (Python 3.11+)
- **Realtime**: FastAPI + WebSocket + Redis Pub/Sub
- **Frontend**: React 18 + TypeScript + Vite
- **AI Chatbot**: FastAPI + LLM API
- **DB**: PostgreSQL 16
- **Cache/Pub-Sub**: Redis 7
- **Containerization**: Docker + Docker Compose

## 시작하기

### 1. 환경 변수 설정

```bash
cp .env.example .env
# .env 파일을 열어 각 값 수정
```

### 2. 빌드 및 실행

```bash
# 프로덕션
docker compose up --build

# 개발 환경 (hot reload 지원)
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### 3. 각 서비스 접속

- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs
- Realtime Server docs: http://localhost:8001/docs
- AI Chatbot docs: http://localhost:8002/docs

## 폴더 구조

```
.
├── backend/          # FastAPI REST API (개발자 1)
├── realtime/         # WebSocket 실시간 서버 (개발자 2)
├── frontend/         # React 프론트엔드 (개발자 3)
├── ai-chatbot/       # AI 챗봇 서비스 (개발자 4)
├── database/         # DB 마이그레이션 & 시드 (개발자 3)
├── docs/             # 공통 문서
├── docker-compose.yml
├── docker-compose.dev.yml
└── .env.example
```

## 서비스 간 통신

```
Frontend (3000)
  ├── REST API  →  Backend (8000)
  ├── WebSocket →  Realtime (8001)
  └── REST API  →  AI Chatbot (8002)

Backend (8000)
  ├── DB        →  PostgreSQL (5432)
  └── Pub/Sub   →  Redis (6379)

Realtime (8001)
  ├── DB        →  PostgreSQL (5432)
  └── Pub/Sub   →  Redis (6379)

AI Chatbot (8002)
  └── DB        →  PostgreSQL (5432)
```

## 브랜치 전략

- `main`: 프로덕션 배포 브랜치
- `develop`: 통합 개발 브랜치
- `feature/<이름>/<기능>`: 기능 개발 브랜치
- 예시: `feature/backend/auth`, `feature/frontend/dashboard`
