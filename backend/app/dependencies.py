from typing import Annotated

from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from sqlmodel import Session

from .crud.chat import ChatCRUD
from .crud.document import DocumentCRUD
from .crud.message import MessageCRUD
from .crud.user import UserCRUD
from .schemas.user import User
from .settings import Settings, settings
from .utils.database import engine
from .utils.passwords import PasswordUtils


def get_session():
    with Session(engine) as session:
        yield session


def get_password_utils() -> PasswordUtils:
    return PasswordUtils(settings)


def get_settings() -> Settings:
    return settings


SessionDep = Annotated[Session, Depends(get_session)]
PasswordUtilsDep = Annotated[PasswordUtils, Depends(get_password_utils)]
SettingsDep = Annotated[Settings, Depends(get_settings)]


def get_user_crud() -> UserCRUD:
    return UserCRUD()


def get_chat_crud() -> ChatCRUD:
    return ChatCRUD()


def get_message_crud() -> MessageCRUD:
    return MessageCRUD()


def get_document_crud() -> DocumentCRUD:
    return DocumentCRUD()


def get_oauth2_scheme(
    password_utils: PasswordUtils = Depends(get_password_utils),
):
    return password_utils.oauth2_scheme


async def get_current_user(
    password_utils: Annotated[PasswordUtils, Depends(get_password_utils)],
    token: Annotated[str, Depends(get_oauth2_scheme)],
    user_crud: Annotated[UserCRUD, Depends(get_user_crud)],
    session: Annotated[Session, Depends(get_session)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data = password_utils.decode_token(token)
    except InvalidTokenError:
        raise credentials_exception
    user = user_crud.get_user_by_email(session, token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
