from app.utils import response_ok
from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.features.auth.service import auth_service
from app.features.auth.schemas import Token
from app.features.auth.dependencies import get_current_user
from app.features.users.schemas import UserRead, UserCreate
from app.features.users.crud import user as crud_user
from app.config import settings
from app.core import security
from app.core.exceptions import AppException
from app.core.base_schema import BaseResponse

router = APIRouter()

@router.post("/login", response_model=BaseResponse[Token])
async def login(
    session: AsyncSession = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = await auth_service.authenticate(
        session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise AppException(message="Incorrect email or password", status_code=status.HTTP_400_BAD_REQUEST)
    elif not user.is_active:
        raise AppException(message="Inactive user", status_code=status.HTTP_400_BAD_REQUEST)
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = Token(
        access_token=security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        token_type="bearer",
    )
    return response_ok(data=token_data, message="Login successful")

@router.post("/register", response_model=BaseResponse[UserRead])
async def register(
    *,
    session: AsyncSession = Depends(get_session),
    user_in: UserCreate,
) -> Any:
    user = await crud_user.get_by_email(session, email=user_in.email)
    if user:
        raise AppException(
            message="The user with this email already exists in the system.",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    user = await auth_service.register(session, user_in=user_in)
    return response_ok(data=user, message="Register successful")

@router.get("/me", response_model=BaseResponse[UserRead])
async def read_user_me(
    current_user: UserRead = Depends(get_current_user),
) -> Any:
    return response_ok(data=current_user)
