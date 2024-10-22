from fastapi import APIRouter, Depends, HTTPException, status

from ..crud.user import UserCRUD
from ..dependencies import SessionDep, get_user_crud
from ..schemas.user import UserCreate, UserOut, UserUpdate

router = APIRouter(
    prefix="/users", tags=["users"], dependencies=[Depends(get_user_crud)]
)


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    session: SessionDep,
    user_crud: UserCRUD = Depends(),
) -> UserOut:
    db_user = user_crud.get_user_by_email(session, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return user_crud.create(session, obj_in=user)


@router.get(
    "/",
    response_model=list[UserOut],
    status_code=status.HTTP_200_OK,
)
async def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: int = 100,
    user_crud: UserCRUD = Depends(),
) -> list[UserOut]:
    users = user_crud.get_all(session, offset, limit)
    return users


@router.get(
    "/{user_id}",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def read_user(
    user_id: int,
    session: SessionDep,
    user_crud: UserCRUD = Depends(),
) -> UserOut:
    db_user = user_crud.get(session, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put(
    "/{user_id}",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def update_user(
    user_id: int,
    user: UserUpdate,
    session: SessionDep,
    user_crud: UserCRUD = Depends(),
) -> UserOut:
    db_user = user_crud.update(session, user_id, user)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return db_user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_user(
    user_id: int,
    session: SessionDep,
    user_crud: UserCRUD = Depends(),
) -> dict:
    db_user = user_crud.delete(session, user_id)
    if db_user is None:
        raise HTTPException()
    return {"message": "User deleted successfully"}
