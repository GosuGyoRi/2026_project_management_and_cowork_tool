from app.core.config import settings
from app.schemas.chat import ChatMessage, ChatResponse

SYSTEM_PROMPT = """당신은 프로젝트 관리 협업 도구의 AI 어시스턴트입니다.
사용자의 업무, 프로젝트, 일정 관리를 도와주세요.
- 업무 우선순위 설정
- 일정 계획
- 팀 협업 방법 제안
- 진행 상황 분석 및 리포트
답변은 간결하고 실용적으로 해주세요."""


async def generate_reply(message: str, history: list[ChatMessage], context: dict) -> ChatResponse:
    if settings.LLM_PROVIDER == "anthropic":
        return await _call_anthropic(message, history, context)
    return await _call_openai(message, history, context)


async def _call_openai(message: str, history: list[ChatMessage], context: dict) -> ChatResponse:
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for h in history:
        messages.append({"role": h.role, "content": h.content})
    messages.append({"role": "user", "content": message})

    response = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=messages,
    )
    return ChatResponse(reply=response.choices[0].message.content or "")


async def _call_anthropic(message: str, history: list[ChatMessage], context: dict) -> ChatResponse:
    import anthropic
    client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

    messages = [{"role": h.role, "content": h.content} for h in history]
    messages.append({"role": "user", "content": message})

    response = await client.messages.create(
        model=settings.ANTHROPIC_MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    return ChatResponse(reply=response.content[0].text)
