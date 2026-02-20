from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_sports():
    return {"message": "List of sports"}
