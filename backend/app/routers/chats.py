from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.chat import ChatCRUD
from ..dependencies import SessionDep, get_chat_crud
from ..schemas.chat import ChatCreate, ChatOut, ChatUpdate

router = APIRouter(
    prefix="/chats", tags=["chats"], dependencies=[Depends(get_chat_crud)]
)


@router.post("/", response_model=ChatOut)
def create_chat(
    chat: ChatCreate,
    session: SessionDep,
    chat_crud: ChatCRUD = Depends(),
):
    return chat_crud.create(session, chat)


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


@router.get("/{chat_id}", response_model=ChatOut)
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
