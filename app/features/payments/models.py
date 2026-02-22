from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from app.constants.enums import PaymentStatus

class PaymentBase(SQLModel):
    booking_id: int = Field(foreign_key="bookings.id")
    amount: float
    status: PaymentStatus = Field(default=PaymentStatus.PENDING)

class Payment(PaymentBase, table=True):
    __tablename__ = "payments"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
