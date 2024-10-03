from pydantic import BaseModel, EmailStr, Field


class ItemBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Foo",
                    "description": "A very nice Item",
                }
            ]
        }
    }


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "a@b.com",
                }
            ]
        }
    }


class UserCreate(UserBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    **UserBase.model_config["json_schema_extra"]["examples"][
                        0
                    ],
                    "password": "secret",
                }
            ]
        }
    }


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
        json_schema_extra = {
            "examples": [
                {
                    **UserBase.model_config["json_schema_extra"]["examples"][
                        0
                    ],
                    "is_active": True,
                    "items": [],
                }
            ]
        }
