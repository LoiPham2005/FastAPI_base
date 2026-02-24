from typing import Optional
from app.core.base_schema import BaseSchema

class UserCreate(BaseSchema):
    email: str
    full_name: str
    password: str
    is_superuser: Optional[bool] = False

class UserUpdate(BaseSchema):
    full_name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None

class UserRead(BaseSchema):
    id: int
    email: str
    full_name: str
    is_active: bool
    is_superuser: bool
