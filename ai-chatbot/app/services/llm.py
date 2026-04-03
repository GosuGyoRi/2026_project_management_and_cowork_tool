import anthropic
from typing import List

from app.core.config import settings
from app.schemas.chat import ChatMessage, ChatResponse, TokenUsage


class LLMService:
    """Claude API를 래핑하는 LLM 서비스"""

    def __init__(self) -> None:
        self._client: anthropic.AsyncAnthropic | None = None

    @property
    def client(self) -> anthropic.AsyncAnthropic:
        if self._client is None:
            self._client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
        return self._client

    async def chat(
        self,
        messages: List[ChatMessage],
        system_prompt: str | None = None,
    ) -> ChatResponse:
        """
        Claude API에 메시지를 전송하고 응답을 반환합니다.

        Args:
            messages: 대화 히스토리
            system_prompt: 커스텀 시스템 프롬프트 (None이면 기본값)

        Returns:
            ChatResponse: AI 응답 + 토큰 사용량
        """
        system = system_prompt or settings.SYSTEM_PROMPT

        response = await self.client.messages.create(
            model=settings.CLAUDE_MODEL,
            max_tokens=settings.CLAUDE_MAX_TOKENS,
            system=system,
            messages=[
                {"role": msg.role.value, "content": msg.content}
                for msg in messages
            ],
        )

        # 텍스트 블록 추출
        assistant_text = "\n".join(
            block.text for block in response.content if block.type == "text"
        )

        return ChatResponse(
            message=assistant_text,
            usage=TokenUsage(
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
            ),
        )


# 싱글턴 인스턴스
llm_service = LLMService()
