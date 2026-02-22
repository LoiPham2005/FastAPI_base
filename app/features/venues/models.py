from sqlmodel import SQLModel, Field
from typing import Optional

class VenueBase(SQLModel):
    name: str = Field(index=True)
    address: str
    description: Optional[str] = None
    capacity: int

class Venue(VenueBase, table=True):
    __tablename__ = "venues"
    id: Optional[int] = Field(default=None, primary_key=True)

class VenueCreate(VenueBase):
    pass

class VenueUpdate(SQLModel):
    name: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = None

class VenueRead(VenueBase):
    id: int
