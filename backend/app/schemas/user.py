from pydantic import EmailStr
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from .chat import Chat
from .document import Document
from .message import Message


class UserBase(SQLModel):
    email: EmailStr = Field(index=True, unique=True)
    name: str = Field()
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    __table_args__ = (UniqueConstraint("email", name="uq_user_email"),)
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    chats: list["Chat"] = Relationship(back_populates="owner")
    messages: list["Message"] = Relationship(back_populates="owner")
    documents: list["Document"] = Relationship(back_populates="owner")


class UserOut(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    name: str | None = None
    email: str | None = None
    is_active: bool | None = None
    password: str | None = None
