from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.chat import ChatCRUD
from ..dependencies import SessionDep, get_chat_crud, get_current_active_user
from ..schemas.chat import ChatCreate, ChatOut, ChatOutWithMessages, ChatUpdate
from ..schemas.user import UserOut

router = APIRouter(
    prefix="/chats", tags=["chats"], dependencies=[Depends(get_chat_crud)]
)


@router.post("/", response_model=ChatOut, status_code=status.HTTP_201_CREATED)
def create_chat(
    chat: ChatCreate,
    session: SessionDep,
    current_user: Annotated[UserOut, Depends(get_current_active_user)],
    chat_crud: ChatCRUD = Depends(),
):
    return chat_crud.create(session, chat, current_user.id)


@router.get(
    "/",
    response_model=list[ChatOut],
    status_code=status.HTTP_200_OK,
)
async def read_chats(
    session: SessionDep,
    offset: int = 0,
    limit: int = 100,
    chat_crud: ChatCRUD = Depends(),
) -> list[ChatOut]:
    chats = chat_crud.get_all(session, offset, limit)
    return chats


@router.get("/{chat_id}", response_model=ChatOutWithMessages)
def read_chat(
    chat_id: int,
    session: SessionDep,
    chat_crud: ChatCRUD = Depends(),
):
    db_chat = chat_crud.get(session, chat_id)
    if db_chat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return db_chat


@router.put("/{chat_id}", response_model=ChatOut)
def update_chat(
    chat_id: int,
    chat: ChatUpdate,
    session: SessionDep,
    chat_crud: ChatCRUD = Depends(),
):
    db_chat = chat_crud.update(session, chat_id, chat)
    if db_chat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return db_chat


@router.delete("/{chat_id}")
def delete_chat(
    chat_id: int,
    session: SessionDep,
    chat_crud: ChatCRUD = Depends(),
):
    db_chat = chat_crud.delete(session, chat_id)
    if db_chat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return {"message": "Chat deleted successfully"}


@router.get(
    "/user/{user_id}",
    response_model=list[ChatOut],
    status_code=status.HTTP_200_OK,
)
async def read_user_chats(
    user_id: int,
    session: SessionDep,
    chat_crud: ChatCRUD = Depends(),
) -> list[ChatOut]:
    chats = chat_crud.get_chats_by_user(session, user_id)
    return chats
