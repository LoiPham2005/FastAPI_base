from fastapi import APIRouter

from app.api.v1 import auth, users, venues, bookings, sports, timeslots, payments

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(venues.router, prefix="/venues", tags=["venues"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
api_router.include_router(sports.router, prefix="/sports", tags=["sports"])
api_router.include_router(timeslots.router, prefix="/timeslots", tags=["timeslots"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
