from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.db.session import get_session
from app.features.users.crud import user as crud_user
from app.features.users.models import User
from app.features.auth.schemas import TokenPayload

from app.core.exceptions import AppException

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

async def get_current_user(
    session: AsyncSession = Depends(get_session), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (JWTError, Exception):
        raise AppException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Could not validate credentials",
        )
    user = await crud_user.get(session, id=token_data.sub)
    if not user:
        raise AppException(status_code=status.HTTP_404_NOT_FOUND, message="User not found")
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_active:
        raise AppException(status_code=status.HTTP_400_BAD_REQUEST, message="Inactive user")
    return current_user

async def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_superuser:
        raise AppException(
            status_code=status.HTTP_403_FORBIDDEN, message="The user doesn't have enough privileges"
        )
    return current_user
