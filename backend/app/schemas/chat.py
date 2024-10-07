from pydantic import BaseModel


class ChatBase(BaseModel):
    title: str


class ChatCreate(ChatBase):
    pass


class ChatUpdate(ChatBase):
    pass


class ChatOut(ChatBase):
    id: int
    owner_id: int
    messages: list[dict] = []

    class Config:
        orm_mode = True
