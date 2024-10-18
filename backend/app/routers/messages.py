from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.message import MessageCRUD
from ..dependencies import SessionDep, get_message_crud
from ..schemas.message import MessageCreate, MessageOut, MessageUpdate

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
    dependencies=[Depends(get_message_crud)],
)


@router.post("/", response_model=MessageOut)
def create_message(
    message: MessageCreate,
    session: SessionDep,
    message_crud: MessageCRUD = Depends(),
):
    return message_crud.create(session, message)


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


@router.delete("/{message_id}")
def delete_message(
    message_id: int, session: SessionDep, message_crud: MessageCRUD = Depends()
):
    db_message = message_crud.delete(session, message_id)
    if db_message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
    return {"message": "Message deleted successfully"}
