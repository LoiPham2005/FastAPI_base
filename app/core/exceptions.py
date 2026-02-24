from typing import Any, Dict, Optional
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.base_schema import BaseResponse
import logging

logger = logging.getLogger("app.exceptions")

class AppException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST, data: Any = None):
        self.message = message
        self.status_code = status_code
        self.data = data

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=BaseResponse(
            success=False,
            message=exc.message,
            data=exc.data
        ).model_dump()
    )

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=BaseResponse(
            success=False,
            message=exc.detail,
        ).model_dump()
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    # Simplify error structure for common use cases
    message = "Validation Error"
    if errors:
        message = f"Field '{errors[0]['loc'][-1]}' {errors[0]['msg']}"
        
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=BaseResponse(
            success=False,
            message=message,
            data=errors
        ).model_dump()
    )

async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=BaseResponse(
            success=False,
            message="Internal Server Error",
        ).model_dump()
    )

def setup_exceptions(app):
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
