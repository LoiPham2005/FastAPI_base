from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_venues():
    return {"message": "List of venues from features/venues"}
