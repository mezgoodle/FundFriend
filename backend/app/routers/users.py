from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..crud.user import UserCRUD
from ..dependencies import get_db, get_user_crud
from ..schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users", tags=["users"], dependencies=[Depends(get_user_crud)]
)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    user_crud: UserCRUD = Depends(),
) -> User:
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return user_crud.create(db=db, obj_in=user)


@router.get(
    "/",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
)
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user_crud: UserCRUD = Depends(),
) -> list[User]:
    users = user_crud.get_all(db, skip=skip, limit=limit)
    return users


@router.get(
    "/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    user_crud: UserCRUD = Depends(),
) -> User:
    db_user = user_crud.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
