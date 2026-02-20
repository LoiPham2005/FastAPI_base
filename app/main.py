from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.features.auth.router import router as auth_router
from app.features.users.router import router as users_router
from app.features.venues.router import router as venues_router
from app.features.bookings.router import router as bookings_router
from app.features.payments.router import router as payments_router

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
    _app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
    _app.include_router(users_router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])
    _app.include_router(venues_router, prefix=f"{settings.API_V1_STR}/venues", tags=["venues"])
    _app.include_router(bookings_router, prefix=f"{settings.API_V1_STR}/bookings", tags=["bookings"])
    _app.include_router(payments_router, prefix=f"{settings.API_V1_STR}/payments", tags=["payments"])

    return _app

app = get_application()

@app.get("/")
def root():
    return {"message": "Welcome to Sports Booking API"}
