from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.v1.router import api_router

def get_application() -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # API Routers
    _app.include_router(api_router, prefix=settings.API_V1_STR)

    return _app

app = get_application()

@app.get("/")
def root():
    return {"message": "Welcome to Sports Booking API"}
