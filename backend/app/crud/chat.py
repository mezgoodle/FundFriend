from sqlalchemy.orm import Session

from .base import CRUD
from .enums import Model


class ChatCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Chat.value)

    def get_chats_by_user(self, db: Session, user_id: int):
        return (
            db.query(self.model).filter(self.model.owner_id == user_id).all()
        )
