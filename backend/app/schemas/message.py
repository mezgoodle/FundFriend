from typing import Optional

from pydantic import BaseModel


# Base модель для спільних полів
class MessageBase(BaseModel):
    message: str


# Модель для створення повідомлення
class MessageCreate(MessageBase):
    chat_id: int


# Модель для оновлення повідомлення
class MessageUpdate(MessageBase):
    chat_id: Optional[int] = None


# Модель для відображення повідомлення
class MessageOut(MessageBase):
    id: int
    chat_id: int
    owner_id: int

    class Config:
        orm_mode = True
