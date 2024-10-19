from sqlmodel import Session, select

from .base import CRUD
from .enums import Model


class MessageCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Message.value)

    def get_message_by_user(self, session: Session, user_id: int):
        statement = select(self.model).where(self.model.owner_id == user_id)
        return session.exec(statement).all()

    def get_messages_by_chat(self, session: Session, chat_id: int):
        statement = select(self.model).where(self.model.chat_id == chat_id)
        return session.exec(statement).all()
