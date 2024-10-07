from typing import Optional

from pydantic import BaseModel


class MessageBase(BaseModel):
    text: str
    chat_id: int


class MessageCreate(MessageBase):
    pass


class MessageUpdate(MessageBase):
    text: Optional[str] = None


class MessageOut(MessageBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
