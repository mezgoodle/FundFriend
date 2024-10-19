from sqlmodel import Session, select

from .base import CRUD
from .enums import Model


class DocumentCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Document.value)

    def get_documents_by_user(self, session: Session, user_id: int):
        statement = select(self.model).where(self.model.owner_id == user_id)
        return session.exec(statement).all()
