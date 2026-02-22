from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.features.venues import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.VenueRead])
async def read_venues(
    session: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return await crud.venue.get_all(session, skip=skip, limit=limit)

@router.post("/", response_model=schemas.VenueRead)
async def create_venue(
    *,
    session: AsyncSession = Depends(get_session),
    venue_in: schemas.VenueCreate,
) -> Any:
    return await crud.venue.create(session, obj_in=venue_in)
