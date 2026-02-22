from typing import Generic, TypeVar, List, Optional
from sqlmodel import SQLModel

T = TypeVar("T")

class BaseResponse(SQLModel, Generic[T]):
    success: bool = True
    message: Optional[str] = None
    data: Optional[T] = None

class PaginatedResponse(SQLModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
