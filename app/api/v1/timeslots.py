from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_timeslots():
    return {"message": "List of timeslots"}
