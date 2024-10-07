from pydantic import BaseModel


class DocumentBase(BaseModel):
    bucket_url: str


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(DocumentBase):
    pass


class DocumentOut(DocumentBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
