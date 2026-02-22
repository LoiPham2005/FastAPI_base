from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional
from app.constants.enums import BookingStatus

class BookingCreate(SQLModel):
    venue_id: int
    start_time: datetime
    end_time: datetime

class BookingUpdate(SQLModel):
    status: Optional[BookingStatus] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

class BookingRead(SQLModel):
    id: int
    user_id: int
    venue_id: int
    start_time: datetime
    end_time: datetime
    status: BookingStatus
    created_at: datetime
