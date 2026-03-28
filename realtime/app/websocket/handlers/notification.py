from fastapi import WebSocket, WebSocketDisconnect
from app.websocket.manager import manager


async def handle(websocket: WebSocket, user_id: str, token: str):
    # TODO: token 검증
    await manager.connect(websocket, f"user:{user_id}")
    try:
        while True:
            await websocket.receive_text()  # keep alive
    except WebSocketDisconnect:
        manager.disconnect(websocket, f"user:{user_id}")
