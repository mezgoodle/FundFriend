from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .message import Message
    from .user import User


class ChatBase(SQLModel):
    title: str
    description: str | None = None
    owner_id: int = Field(foreign_key="user.id", default=None)


class ChatCreate(ChatBase):
    pass


class ChatUpdate(ChatBase):
    title: str | None = None
    description: str | None = None


class ChatOut(ChatBase):
    id: int


class Chat(ChatBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    owner: "User" = Relationship(back_populates="chats")
    messages: list["Message"] = Relationship(back_populates="chat")
