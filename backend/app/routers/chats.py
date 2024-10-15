from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..crud.chat import ChatCRUD
from ..dependencies import get_chat_crud, get_db
from ..schemas.chat import ChatCreate, ChatOut, ChatUpdate

router = APIRouter(
    prefix="/chats", tags=["chats"], dependencies=[Depends(get_chat_crud)]
)


@router.post("/", response_model=ChatOut)
def create_chat(
    chat: ChatCreate,
    db: Session = Depends(get_db),
    chat_crud: ChatCRUD = Depends(),
):
    return chat_crud.create(db, chat)


@router.get(
    "/",
    response_model=list[ChatOut],
    status_code=status.HTTP_200_OK,
)
async def read_chats(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    chat_crud: ChatCRUD = Depends(),
) -> list[ChatOut]:
    chats = chat_crud.get_all(db, skip=skip, limit=limit)
    return chats


@router.get("/{chat_id}", response_model=ChatOut)
def read_chat(
    chat_id: int,
    db: Session = Depends(get_db),
    chat_crud: ChatCRUD = Depends(),
):
    db_chat = chat_crud.get(db, chat_id)
    if db_chat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return db_chat


@router.put("/{chat_id}", response_model=ChatOut)
def update_chat(
    chat_id: int,
    chat: ChatUpdate,
    db: Session = Depends(get_db),
    chat_crud: ChatCRUD = Depends(),
):
    db_chat = chat_crud.update(db, chat_id, chat)
    if db_chat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return db_chat


@router.delete("/{chat_id}")
def delete_chat(
    chat_id: int,
    db: Session = Depends(get_db),
    chat_crud: ChatCRUD = Depends(),
):
    db_chat = chat_crud.delete(db, chat_id)
    if db_chat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    return {"message": "Chat deleted successfully"}
