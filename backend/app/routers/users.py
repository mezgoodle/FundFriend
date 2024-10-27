from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..crud.user import UserCRUD
from ..dependencies import (
    PasswordUtilsDep,
    SessionDep,
    SettingsDep,
    get_current_active_user,
    get_user_crud,
)
from ..schemas.token import Token
from ..schemas.user import UserCreate, UserOut, UserUpdate

router = APIRouter(
    prefix="/users", tags=["users"], dependencies=[Depends(get_user_crud)]
)


@router.post("/login")
async def login_for_access_token(
    session: SessionDep,
    settings: SettingsDep,
    password_utils: PasswordUtilsDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_crud: UserCRUD = Depends(),
) -> Token:
    user_db = user_crud.get_user_by_email(session, form_data.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    authenticated_user = password_utils.authenticate_user(
        user_db, form_data.password
    )
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.access_token_expire_minutes
    )
    access_token = password_utils.create_access_token(
        data={"sub": authenticated_user.email},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=UserOut)
async def read_users_me(
    current_user: Annotated[UserOut, Depends(get_current_active_user)],
):
    return current_user


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    session: SessionDep,
    password_utils: PasswordUtilsDep,
    user_crud: UserCRUD = Depends(),
) -> UserOut:
    db_user = user_crud.get_user_by_email(session, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    user.password = password_utils.get_password_hash(user.password)
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
