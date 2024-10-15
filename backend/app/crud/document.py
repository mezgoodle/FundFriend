from sqlalchemy.orm import Session

from .base import CRUD
from .enums import Model


class DocumentCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Document.value)

    def get_documents_by_user(self, db: Session, user_id: int):
        return (
            db.query(self.model).filter(self.model.owner_id == user_id).all()
        )
