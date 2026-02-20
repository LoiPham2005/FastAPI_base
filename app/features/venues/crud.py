from app.core.base_crud import CRUDBase
from .models import Venue
from .schemas import VenueCreate, VenueUpdate

class CRUDVenue(CRUDBase[Venue, VenueCreate, VenueUpdate]):
    pass

venue = CRUDVenue(Venue)
