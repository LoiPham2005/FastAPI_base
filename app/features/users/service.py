from .crud import user as crud_user

class UserService:
    def get_user(self, db, user_id):
        return crud_user.get(db, user_id)

user_service = UserService()
