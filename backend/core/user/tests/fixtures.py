import pytest

from core.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@gmail.com",
    "first_name": "test",
    "last_name": "user",
    "password": "test1234",
}


@pytest.fixture
def user_db() -> User:
    return User.objects.create_user(**data_user)
