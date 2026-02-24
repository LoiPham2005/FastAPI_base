import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_password
from app.features.users.crud import user as crud_user
from app.features.users.schemas import UserCreate

logger = logging.getLogger("app.auth")

class AuthService:
    async def authenticate(self, session: AsyncSession, email: str, password: str):
        logger.info(f"Authentication attempt for email: {email}")
        user = await crud_user.get_by_email(session, email=email)
        if not user:
            logger.warning(f"Authentication failed: User with email {email} not found")
            return None
        if not verify_password(password, user.hashed_password):
            logger.warning(f"Authentication failed: Invalid password for email {email}")
            return None
        
        logger.info(f"Authentication successful for email: {email}")
        return user

    async def register(self, session: AsyncSession, *, user_in: UserCreate):
        logger.info(f"Registering new user with email: {user_in.email}")
        user = await crud_user.create(session, obj_in=user_in)
        logger.info(f"User registered successfully: {user.email}")
        return user

auth_service = AuthService()
