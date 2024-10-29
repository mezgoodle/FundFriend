from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.message import MessageCRUD
from ..dependencies import (
    SessionDep,
    get_current_active_user,
    get_message_crud,
)
from ..schemas.message import MessageCreate, MessageOut, MessageUpdate
from ..schemas.user import UserOut

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    dependencies=[Depends(get_message_crud)],
)


@router.post(
    "/", response_model=MessageOut, status_code=status.HTTP_201_CREATED
)
def create_message(
    message: MessageCreate,
    session: SessionDep,
    current_user: Annotated[UserOut, Depends(get_current_active_user)],
    message_crud: MessageCRUD = Depends(),
):
    if message := message_crud.create(session, message, current_user.id):
        return message
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error while creating message",
        )


@router.get("/{message_id}", response_model=MessageOut)
def read_message(
    message_id: int, session: SessionDep, message_crud: MessageCRUD = Depends()
):
    db_message = message_crud.get(session, message_id)
    if db_message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return db_message


@router.get(
    "/",
    response_model=list[MessageOut],
    status_code=status.HTTP_200_OK,
)
async def read_messages(
    session: SessionDep,
    offset: int = 0,
    limit: int = 100,
    message_crud: MessageCRUD = Depends(),
) -> list[MessageOut]:
    messages = message_crud.get_all(session, offset, limit)
    return messages


@router.put("/{message_id}", response_model=MessageOut)
def update_message(
    message_id: int,
    message: MessageUpdate,
    session: SessionDep,
    message_crud: MessageCRUD = Depends(),
):
    db_message = message_crud.update(session, message_id, message)
    if db_message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return db_message


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(
    message_id: int, session: SessionDep, message_crud: MessageCRUD = Depends()
):
    db_message = message_crud.delete(session, message_id)
    if db_message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return {"message": "Message deleted successfully"}


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK)
async def read_messages_by_user(
    user_id: int,
    session: SessionDep,
    message_crud: MessageCRUD = Depends(),
) -> list[MessageOut]:
    messages = message_crud.get_messages_by_user(session, user_id)
    return messages


@router.get("/chat/{chat_id}", status_code=status.HTTP_200_OK)
async def read_messages_by_chat(
    chat_id: int,
    session: SessionDep,
    message_crud: MessageCRUD = Depends(),
) -> list[MessageOut]:
    messages = message_crud.get_messages_by_chat(session, chat_id)
    return messages
