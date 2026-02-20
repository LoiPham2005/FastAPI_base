from pydantic import BaseModel

class PaymentCreate(BaseModel):
    booking_id: int
    amount: float

class Payment(PaymentCreate):
    id: int
    status: str
    class Config:
        from_attributes = True
