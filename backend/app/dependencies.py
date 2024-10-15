from .crud.chat import ChatCRUD
from .crud.document import DocumentCRUD
from .crud.message import MessageCRUD
from .crud.user import UserCRUD
from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_crud() -> UserCRUD:
    return UserCRUD()


def get_chat_crud() -> ChatCRUD:
    return ChatCRUD()


def get_message_crud() -> MessageCRUD:
    return MessageCRUD()


def get_document_crud() -> DocumentCRUD:
    return DocumentCRUD()
