from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """AI Chatbot 서비스 설정"""

    # Claude API
    ANTHROPIC_API_KEY: str = ""
    CLAUDE_MODEL: str = "claude-sonnet-4-5-20250929"
    CLAUDE_MAX_TOKENS: int = 4096

    # 서버
    AI_CHATBOT_HOST: str = "0.0.0.0"
    AI_CHATBOT_PORT: int = 8002

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    # 시스템 프롬프트
    SYSTEM_PROMPT: str = (
        "당신은 인력 데이터 분석 전문 AI 어시스턴트입니다.\n\n"
        "역할:\n"
        "- 인력 관련 데이터를 분석하고 인사이트를 도출합니다.\n"
        "- 인원 현황, 채용, 이직률, 부서별 인력 배치 등의 질문에 답변합니다.\n"
        "- 데이터 기반의 객관적인 분석 결과를 제공합니다.\n"
        "- 한국어로 친절하고 전문적으로 응답합니다.\n\n"
        "참고사항:\n"
        "- 사용자가 데이터를 직접 제공하면 그에 기반하여 분석합니다.\n"
        "- 데이터가 없는 경우, 어떤 데이터가 필요한지 안내합니다.\n"
        "- 추후 데이터베이스 연동 시 실제 데이터 분석이 가능합니다."
    )

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
