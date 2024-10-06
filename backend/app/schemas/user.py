from pydantic import BaseModel, EmailStr


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

    class Config:
        orm_mode = True
        json_schema_extra = {
            "examples": [
                {
                    **UserBase.model_config["json_schema_extra"]["examples"][
                        0
                    ],
                    "is_active": True,
                }
            ]
        }
