from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    AI_CHATBOT_PORT: int = 8002
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    SECRET_KEY: str = "changeme"
    ALGORITHM: str = "HS256"

    # LLM
    LLM_PROVIDER: str = "openai"  # openai | anthropic
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o"
    ANTHROPIC_API_KEY: str = ""
    ANTHROPIC_MODEL: str = "claude-sonnet-4-6"

    # DB
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "cowork_db"
    POSTGRES_USER: str = "cowork_user"
    POSTGRES_PASSWORD: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
