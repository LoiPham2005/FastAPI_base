from fastapi import APIRouter

from app.features.auth.router import router as auth_router
from app.features.users.router import router as users_router
from app.features.venues.router import router as venues_router
from app.features.bookings.router import router as bookings_router
from app.features.payments.router import router as payments_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(venues_router, prefix="/venues", tags=["venues"])
api_router.include_router(bookings_router, prefix="/bookings", tags=["bookings"])
api_router.include_router(payments_router, prefix="/payments", tags=["payments"])
