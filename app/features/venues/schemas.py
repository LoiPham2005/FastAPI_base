from pydantic import BaseModel
from typing import Optional

class VenueBase(BaseModel):
    name: str
    address: str

class VenueCreate(VenueBase):
    pass

class VenueUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class Venue(VenueBase):
    id: int
    class Config:
        from_attributes = True
