from pydantic import BaseModel
from sqlalchemy.orm import Session

from .enums import Model


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
