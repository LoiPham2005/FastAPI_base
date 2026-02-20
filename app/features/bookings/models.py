from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.base import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    venue_id = Column(Integer, ForeignKey("venues.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(String, default="pending")
