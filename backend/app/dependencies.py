from .crud import UserCRUD
from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_crud() -> UserCRUD:
    return UserCRUD()
