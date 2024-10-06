from typing import Optional

from pydantic import BaseModel


# Base модель для спільних полів
class DocumentBase(BaseModel):
    bucket_url: str


# Модель для створення документа
class DocumentCreate(DocumentBase):
    pass


# Модель для оновлення документа
class DocumentUpdate(DocumentBase):
    pass


# Модель для відображення документа
class DocumentOut(DocumentBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
