from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from ..schemas.chat import ChatCreate, ChatOut, ChatUpdate

router = APIRouter(prefix="/chats", tags=["chats"])


@router.post("/", response_model=ChatOut)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    return crud.create_chat(db=db, chat=chat)


@router.get("/{chat_id}", response_model=ChatOut)
def read_chat(chat_id: int, db: Session = Depends(get_db)):
    db_chat = crud.get_chat(db, chat_id=chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat


@router.put("/{chat_id}", response_model=ChatOut)
def update_chat(chat_id: int, chat: ChatUpdate, db: Session = Depends(get_db)):
    db_chat = crud.update_chat(db=db, chat_id=chat_id, chat=chat)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat


@router.delete("/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    db_chat = crud.delete_chat(db=db, chat_id=chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"message": "Chat deleted successfully"}
