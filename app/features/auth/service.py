from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_password, create_access_token
from app.features.users.crud import user as crud_user
from app.features.users.schemas import UserCreate

class AuthService:
    async def authenticate(self, session: AsyncSession, email: str, password: str):
        user = await crud_user.get_by_email(session, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def register(self, session: AsyncSession, *, user_in: UserCreate):
        return await crud_user.create(session, obj_in=user_in)

auth_service = AuthService()
