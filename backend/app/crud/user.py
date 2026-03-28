from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.user import User
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User]):
    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def authenticate(self, db: AsyncSession, email: str, password: str) -> User | None:
        user = await self.get_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    async def create_user(self, db: AsyncSession, email: str, username: str, full_name: str, password: str) -> User:
        return await self.create(db, {
            "email": email,
            "username": username,
            "full_name": full_name,
            "hashed_password": get_password_hash(password),
        })


crud_user = CRUDUser(User)
