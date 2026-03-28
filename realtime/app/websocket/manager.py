import json
from collections import defaultdict
from fastapi import WebSocket


class ConnectionManager:
    """WebSocket 연결 관리 - 채널별 연결 유지 및 브로드캐스트"""

    def __init__(self):
        # channel_id -> list of WebSocket
        self._connections: dict[str, list[WebSocket]] = defaultdict(list)

    async def connect(self, websocket: WebSocket, channel_id: str):
        await websocket.accept()
        self._connections[channel_id].append(websocket)

    def disconnect(self, websocket: WebSocket, channel_id: str):
        self._connections[channel_id].remove(websocket)

    async def broadcast(self, channel_id: str, message: dict):
        payload = json.dumps(message)
        for ws in self._connections.get(channel_id, []):
            await ws.send_text(payload)

    async def send_personal(self, websocket: WebSocket, message: dict):
        await websocket.send_text(json.dumps(message))


manager = ConnectionManager()
