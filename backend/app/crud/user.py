from sqlalchemy.orm import Session

from ..schemas.user import UserCreate
from .base import CRUD
from .enums import Model


class UserCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.User.value)

    def get_user_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()

    def create(self, db: Session, obj_in: UserCreate):
        hashed_password = obj_in.password + "notreallyhashed"
        del obj_in.password
        return super().create(db, obj_in, {"hashed_password": hashed_password})
