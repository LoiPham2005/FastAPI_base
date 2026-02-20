from app.core.security import verify_password, get_password_hash, create_access_token
from app.features.users.crud import user as crud_user
from sqlalchemy.orm import Session

class AuthService:
    def authenticate(self, db: Session, email: str, password: str):
        user = crud_user.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

auth_service = AuthService()
