from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.features.users import crud, schemas
from app.features.auth.dependencies import get_current_active_superuser

router = APIRouter()

@router.get("/", response_model=List[schemas.UserRead])
async def read_users(
    session: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = await crud.user.get_all(session, skip=skip, limit=limit)
    return users

@router.post("/", response_model=schemas.UserRead)
async def create_user(
    *,
    session: AsyncSession = Depends(get_session),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = await crud.user.get_by_email(session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = await crud.user.create(session, obj_in=user_in)
    return user
