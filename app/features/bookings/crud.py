from app.core.base_crud import BaseCRUD
from .models import Booking
from .schemas import BookingCreate, BookingUpdate

class CRUDBooking(BaseCRUD[Booking, BookingCreate, BookingUpdate]):
    pass

booking = CRUDBooking(Booking)
