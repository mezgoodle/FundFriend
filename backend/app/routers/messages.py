from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import get_db
from ..schemas.message import MessageCreate, MessageOut, MessageUpdate

router = APIRouter(prefix="/messages", tags=["messages"])


@router.post("/", response_model=MessageOut)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)


@router.get("/{message_id}", response_model=MessageOut)
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message


@router.put("/{message_id}", response_model=MessageOut)
def update_message(
    message_id: int,
    message: MessageUpdate,
    db: Session = Depends(get_db),
):
    db_message = crud.update_message(
        db=db, message_id=message_id, message=message
    )
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message


@router.delete("/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.delete_message(db=db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": "Message deleted successfully"}
