# 시스템 아키텍처

## 서비스 구성도

```
                          ┌─────────────────┐
                          │    Frontend      │
                          │ React + TS       │
                          │  :3000           │
                          └────────┬────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
    │    Backend        │  │    Realtime       │  │   AI Chatbot     │
    │  FastAPI REST     │  │  FastAPI WS       │  │   FastAPI        │
    │    :8000          │  │    :8001          │  │    :8002         │
    └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘
             │                     │                      │
             ▼                     ▼                      │
    ┌──────────────────┐  ┌──────────────────┐           │
    │   PostgreSQL      │  │     Redis         │           │
    │    :5432          │  │    :6379          │           │
    └──────────────────┘  └──────────────────┘           │
             ▲                                             │
             └─────────────────────────────────────────────┘
```

## 데이터 흐름

### 인증 흐름
1. 사용자 로그인 요청 → Backend `/api/v1/auth/login`
2. JWT 토큰 발급 → Frontend localStorage 저장
3. 이후 모든 API 요청에 `Authorization: Bearer <token>` 헤더 첨부

### 실시간 채팅 흐름
1. Frontend → WebSocket 연결: `ws://realtime:8001/ws/chat/{channel_id}?token=<jwt>`
2. 메시지 전송 → Realtime 서버가 Redis Pub/Sub으로 브로드캐스트
3. 같은 채널의 모든 연결된 클라이언트에게 전달

### AI 챗봇 흐름
1. 사용자 질문 → `POST /api/chat/`
2. AI Chatbot 서버가 LLM API 호출
3. 응답 반환

## 담당자별 개발 영역

| 담당자 | 서비스 | 주요 파일 |
|--------|--------|-----------|
| 개발자 1 | backend/ | `app/api/`, `app/crud/`, `app/models/` |
| 개발자 2 | realtime/ | `app/websocket/` |
| 개발자 3 | frontend/, database/ | `src/`, `migrations/` |
| 개발자 4 | ai-chatbot/ | `app/services/`, `app/api/` |
