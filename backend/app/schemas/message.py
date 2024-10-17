from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .chat import Chat
    from .user import User


class MessageBase(SQLModel):
    text: str


class MessageCreate(MessageBase):
    pass


class MessageUpdate(SQLModel):
    text: str | None = None


class MessageOut(MessageBase):
    id: int


class Message(MessageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    chat_id: int = Field(foreign_key="chat.id")
    owner_id: int = Field(foreign_key="user.id")
    chat: "Chat" = Relationship(back_populates="messages")
    owner: "User" = Relationship(back_populates="messages")
