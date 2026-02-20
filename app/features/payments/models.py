from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    amount = Column(Float)
    status = Column(String)
    transaction_id = Column(String)
