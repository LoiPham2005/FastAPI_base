from app.core.base_crud import CRUDBase
from .models import Booking
from .schemas import BookingCreate

class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingCreate]):
    pass

booking = CRUDBooking(Booking)
