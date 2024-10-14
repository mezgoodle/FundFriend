from enum import Enum

from pydantic import BaseModel
from sqlalchemy.orm import Session

from .models import Chat, Document, Message, User
from .schemas.user import UserCreate


class Model(Enum):
    User = User
    Chat = Chat
    Message = Message
    Document = Document


class CRUD:
    def __init__(self, model: Model):
        self.model = model

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, limit: int = 100, skip: int = 0):
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(
        self, db: Session, obj_in: BaseModel, additional_data: dict = None
    ):
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data, **additional_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, id: int, obj_in: BaseModel):
        obj = db.query(self.model).filter(self.model.id == id).first()
        obj_in_data = obj_in.dict(exclude_unset=True)
        for field in obj_in_data:
            setattr(obj, field, obj_in_data[field])
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, id: int):
        obj = db.query(self.model).filter(self.model.id == id).first()
        db.delete(obj)
        db.commit()
        return obj


class UserCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.User.value)

    def get_user_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()

    def create(self, db: Session, obj_in: UserCreate):
        hashed_password = obj_in.password + "notreallyhashed"
        del obj_in.password
        return super().create(db, obj_in, {"hashed_password": hashed_password})
