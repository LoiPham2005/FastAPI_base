from sqlmodel import SQLModel
from typing import Optional
from app.constants.enums import PaymentStatus

class PaymentCreate(SQLModel):
    booking_id: int
    amount: float

class PaymentUpdate(SQLModel):
    status: Optional[PaymentStatus] = None

class PaymentRead(SQLModel):
    id: int
    booking_id: int
    amount: float
    status: PaymentStatus
    created_at: datetime
