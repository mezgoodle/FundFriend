from sqlalchemy.orm import Session

from .base import CRUD
from .enums import Model


class MessageCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Message.value)

    def get_message_by_user(self, db: Session, user_id: int):
        return (
            db.query(self.model).filter(self.model.owner_id == user_id).all()
        )

    def get_messages_by_chat(self, db: Session, chat_id: int):
        return db.query(self.model).filter(self.model.chat_id == chat_id).all()
