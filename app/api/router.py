from fastapi import APIRouter

from app.features.auth import router as auth
from app.features.users import router as users
from app.features.venues import router as venues
from app.features.bookings import router as bookings
from app.features.payments import router as payments

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(venues.router, prefix="/venues", tags=["venues"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
