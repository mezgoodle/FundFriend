from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class DocumentBase(SQLModel):
    bucket_url: str
    name: str


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(SQLModel):
    bucket_url: str | None = None
    name: str | None = None


class DocumentOut(DocumentBase):
    id: int
    owner_id: int


class Document(DocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id", default=None)
    owner: "User" = Relationship(back_populates="documents")
