from datetime import datetime
from typing import Optional
from app.core.base_schema import BaseSchema
from app.constants.enums import PaymentStatus

class PaymentCreate(BaseSchema):
    booking_id: int
    amount: float

class PaymentUpdate(BaseSchema):
    status: Optional[PaymentStatus] = None

class PaymentRead(BaseSchema):
    id: int
    booking_id: int
    amount: float
    status: PaymentStatus
    created_at: datetime
