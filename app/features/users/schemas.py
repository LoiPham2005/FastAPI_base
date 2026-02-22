from sqlmodel import SQLModel
from typing import Optional

class UserCreate(SQLModel):
    email: str
    full_name: str
    password: str
    is_superuser: Optional[bool] = False

class UserUpdate(SQLModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None

class UserRead(SQLModel):
    id: int
    email: str
    full_name: str
    is_active: bool
    is_superuser: bool
