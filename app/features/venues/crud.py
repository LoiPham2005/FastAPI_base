from app.core.base_crud import BaseCRUD
from .models import Venue
from .schemas import VenueCreate, VenueUpdate

class CRUDVenue(BaseCRUD[Venue, VenueCreate, VenueUpdate]):
    pass

venue = CRUDVenue(Venue)
