from typing import List, Optional

from pydantic import BaseModel


# Base модель для спільних полів
class ChatBase(BaseModel):
    message: str


# Модель для створення чату
class ChatCreate(ChatBase):
    pass


# Модель для оновлення чату
class ChatUpdate(ChatBase):
    pass


# Модель для відображення чату (включаючи пов'язані повідомлення)
class ChatOut(ChatBase):
    id: int
    owner_id: int
    messages: List[dict] = []

    class Config:
        orm_mode = True
