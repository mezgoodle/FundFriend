from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/items", tags=["items"])


@router.post(
    "/{user_id}/",
    response_model=schemas.Item,
    status_code=status.HTTP_201_CREATED,
)
async def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
) -> schemas.Item:
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get(
    "/",
    response_model=list[schemas.Item],
    status_code=status.HTTP_200_OK,
)
async def read_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> list[schemas.Item]:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
