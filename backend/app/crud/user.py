from sqlmodel import Session, select

from ..schemas.user import UserCreate
from .base import CRUD
from .enums import Model


class UserCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.User.value)

    def get_user_by_email(self, session: Session, email: str):
        statement = select(self.model).where(self.model.email == email)
        return session.exec(statement).first()

    def create(self, db: Session, obj_in: UserCreate):
        hashed_password = obj_in.password + "notreallyhashed"
        del obj_in.password
        return super().create(db, obj_in, {"hashed_password": hashed_password})
