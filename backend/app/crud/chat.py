from sqlmodel import Session, select

from .base import CRUD
from .enums import Model


class ChatCRUD(CRUD):
    def __init__(self):
        super().__init__(Model.Chat.value)

    def get_chats_by_user(self, session: Session, user_id: int):
        statement = select(self.model).where(self.model.owner_id == user_id)
        return session.exec(statement).all()
