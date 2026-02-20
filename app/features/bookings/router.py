from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_bookings():
    return {"message": "List of bookings from features/bookings"}
