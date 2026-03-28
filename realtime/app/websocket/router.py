from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from app.websocket.manager import manager
from app.websocket.handlers import chat, notification, presence

ws_router = APIRouter()


@ws_router.websocket("/ws/chat/{channel_id}")
async def websocket_chat(websocket: WebSocket, channel_id: str, token: str = Query(...)):
    await chat.handle(websocket, channel_id, token)


@ws_router.websocket("/ws/notifications/{user_id}")
async def websocket_notifications(websocket: WebSocket, user_id: str, token: str = Query(...)):
    await notification.handle(websocket, user_id, token)


@ws_router.websocket("/ws/presence/{workspace_id}")
async def websocket_presence(websocket: WebSocket, workspace_id: str, token: str = Query(...)):
    await presence.handle(websocket, workspace_id, token)
