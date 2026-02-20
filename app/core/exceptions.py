from fastapi import Request
from fastapi.responses import JSONResponse

class AppException(Exception):
    def __init__(self, name: str):
        self.name = name

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
