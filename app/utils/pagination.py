from typing import Generic, TypeVar, List
from sqlmodel import SQLModel

T = TypeVar("T")

class PaginatedResponse(SQLModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int

def paginate(items: List[T], total: int, page: int, size: int) -> PaginatedResponse[T]:
    return PaginatedResponse(
        items=items,
        total=total,
        page=page,
        size=size
    )
