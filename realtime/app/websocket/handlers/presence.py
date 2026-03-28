import json
from fastapi import WebSocket, WebSocketDisconnect
from app.websocket.manager import manager


async def handle(websocket: WebSocket, workspace_id: str, token: str):
    # TODO: token 검증
    channel_key = f"presence:{workspace_id}"
    await manager.connect(websocket, channel_key)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await manager.broadcast(channel_key, {
                "type": "presence_update",
                "user_id": message.get("user_id"),
                "status": message.get("status"),  # online / away / offline
            })
    except WebSocketDisconnect:
        manager.disconnect(websocket, channel_key)
