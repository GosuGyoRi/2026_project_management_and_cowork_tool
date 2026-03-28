from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# 모든 모델을 여기서 import해야 Alembic이 마이그레이션을 감지합니다
from app.models import *  # noqa: F401, E402
