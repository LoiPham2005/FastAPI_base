from typing import Any, Optional
from app.core.base_schema import BaseResponse

def to_camel(string: str) -> str:
    return "".join(word.capitalize() for word in string.split("_"))

def to_snake(string: str) -> str:
    return "".join(["_" + i.lower() if i.isupper() else i for i in string]).lstrip("_")

def response_ok(data: Any = None, message: str = "Success") -> BaseResponse:
    return BaseResponse(success=True, message=message, data=data)

def response_error(message: str = "Error", data: Any = None) -> BaseResponse:
    return BaseResponse(success=False, message=message, data=data)
