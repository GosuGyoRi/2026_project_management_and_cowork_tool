from pydantic import BaseModel
from typing import Literal


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = []
    context: dict = {}  # 현재 프로젝트/업무 컨텍스트


class ChatResponse(BaseModel):
    reply: str
    suggestions: list[str] = []
