from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from .crud.chat import ChatCRUD
from .crud.document import DocumentCRUD
from .crud.message import MessageCRUD
from .crud.user import UserCRUD
from .database import engine


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def get_user_crud() -> UserCRUD:
    return UserCRUD()


def get_chat_crud() -> ChatCRUD:
    return ChatCRUD()


def get_message_crud() -> MessageCRUD:
    return MessageCRUD()


def get_document_crud() -> DocumentCRUD:
    return DocumentCRUD()
