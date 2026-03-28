import json
from fastapi import WebSocket, WebSocketDisconnect
from app.websocket.manager import manager


async def handle(websocket: WebSocket, channel_id: str, token: str):
    # TODO: token 검증
    await manager.connect(websocket, channel_id)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            # 채널 전체에 브로드캐스트
            await manager.broadcast(channel_id, {
                "type": "chat_message",
                "channel_id": channel_id,
                "content": message.get("content"),
                "sender_id": message.get("sender_id"),
            })
    except WebSocketDisconnect:
        manager.disconnect(websocket, channel_id)
