from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from app.constants.enums import BookingStatus

class BookingBase(SQLModel):
    user_id: int = Field(foreign_key="users.id")
    venue_id: int = Field(foreign_key="venues.id")
    start_time: datetime
    end_time: datetime
    status: BookingStatus = Field(default=BookingStatus.PENDING)

class Booking(BookingBase, table=True):
    __tablename__ = "bookings"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
