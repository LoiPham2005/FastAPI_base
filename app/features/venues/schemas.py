from sqlmodel import SQLModel
from typing import Optional

class VenueCreate(SQLModel):
    name: str
    address: str
    description: Optional[str] = None
    capacity: int

class VenueUpdate(SQLModel):
    name: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = None

class VenueRead(SQLModel):
    id: int
    name: str
    address: str
    description: Optional[str] = None
    capacity: int
