from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.features.bookings import crud, schemas
from app.features.auth.dependencies import get_current_active_user

router = APIRouter()

@router.get("/", response_model=List[schemas.BookingRead])
async def read_bookings(
    session: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return await crud.booking.get_all(session, skip=skip, limit=limit)

@router.post("/", response_model=schemas.BookingRead)
async def create_booking(
    *,
    session: AsyncSession = Depends(get_session),
    booking_in: schemas.BookingCreate,
    current_user: Any = Depends(get_current_active_user),
) -> Any:
    # Basic logic: create booking for current user
    # In real world, check if venue exists and is available
    from app.features.bookings.models import Booking
    db_obj = Booking(
        **booking_in.model_dump(),
        user_id=current_user.id
    )
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
