from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.features.payments import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.PaymentRead])
async def read_payments(
    session: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return await crud.payment.get_all(session, skip=skip, limit=limit)
