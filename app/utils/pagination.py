from typing import Generic, TypeVar, List
from pydantic import BaseModel

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int

def paginate(items: List[T], page: int, size: int) -> Page[T]:
    start = (page - 1) * size
    end = start + size
    return Page(
        items=items[start:end],
        total=len(items),
        page=page,
        size=size
    )
