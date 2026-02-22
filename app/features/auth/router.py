from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
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

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(
    session: AsyncSession = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = await auth_service.authenticate(
        session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/register", response_model=UserRead)
async def register(
    *,
    session: AsyncSession = Depends(get_session),
    user_in: UserCreate,
) -> Any:
    user = await crud_user.get_by_email(session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = await auth_service.register(session, user_in=user_in)
    return user

@router.get("/me", response_model=UserRead)
async def read_user_me(
    current_user: UserRead = Depends(get_current_user),
) -> Any:
    return current_user
