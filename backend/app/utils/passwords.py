from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from ..schemas.token import TokenData
from ..schemas.user import User
from ..settings import Settings


class PasswordUtils:
    def __init__(self, settings: Settings):
        self.secret_key = settings.hash_secret_key
        self.algorithm = settings.hash_algorithm
        self.access_token_expire_minutes = settings.access_token_expire_minutes
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def authenticate_user(self, user: User | None, password: str):
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(
        self, data: dict, expires_delta: timedelta | None = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, self.secret_key, algorithm=self.algorithm
        )
        return encoded_jwt

    def decode_token(self, token: str) -> TokenData | None:
        payload = jwt.decode(
            token, self.secret_key, algorithms=[self.algorithm]
        )
        email: str = payload.get("sub")
        return TokenData(email=email) if email else None
