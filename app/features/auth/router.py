from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "login from features/auth"}

@router.post("/register")
def register():
    return {"message": "register from features/auth"}
