from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.core.base_crud import BaseCRUD
from .models import User
from .schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash

class CRUDUser(BaseCRUD[User, UserCreate, UserUpdate]):
    async def get_by_email(self, session: AsyncSession, *, email: str) -> Optional[User]:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create(self, session: AsyncSession, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser or False,
        )
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

user = CRUDUser(User)
