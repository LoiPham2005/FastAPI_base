from typing import Generic, TypeVar, List, Optional, Any
from sqlmodel import SQLModel
from pydantic import ConfigDict

T = TypeVar("T")

class BaseSchema(SQLModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        str_strip_whitespace=True
    )

class BaseResponse(BaseSchema, Generic[T]):
    success: bool = True
    message: Optional[str] = "Success"
    data: Optional[T] = None

class ErrorResponse(BaseSchema):
    success: bool = False
    message: str
    errors: Optional[Any] = None

class PaginatedResponse(BaseSchema, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    pages: int
