from typing import Annotated

from fastapi import Query
from pydantic import BaseModel
from sqlmodel import Session, select

from .enums import Model


class CRUD:
    def __init__(self, model: Model):
        self.model = model

    def get(self, session: Session, id: int):
        return session.get(self.model, id)

    def get_all(
        self,
        session: Session,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
    ):
        return session.exec(
            select(self.model).offset(offset).limit(limit)
        ).all()

    def create(
        self, session: Session, obj_in: BaseModel, additional_data: dict = None
    ):
        obj_in_data = obj_in.model_dump()
        if additional_data:
            obj_in_data.update(additional_data)
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def update(self, session: Session, id: int, obj_in: BaseModel):
        obj = session.get(self.model, id)
        if not obj:
            return None
        obj_in_data = obj_in.model_dump(exclude_unset=True)
        obj.sqlmodel_update(obj_in_data)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def delete(self, session: Session, id: int):
        obj = session.get(self.model, id)
        if not obj:
            return None
        session.delete(obj)
        session.commit()
        return {"ok": True}
