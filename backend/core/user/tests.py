import pytest

from core.user.models import User


@pytest.fixture
def user() -> dict:
    return {
        "username": "test_user",
        "email": "test@gmail.com",
        "first_name": "test",
        "last_name": "user",
        "password": "test1234",
    }


@pytest.mark.django_db
def test_create_user(user: dict):
    created_user = User.objects.create_user(**user)
    assert created_user.username == user["username"]
    assert created_user.email == user["email"]
    assert created_user.first_name == user["first_name"]
    assert created_user.last_name == user["last_name"]


@pytest.mark.django_db
def test_create_superuser(user: dict):
    created_user = User.objects.create_superuser(**user)
    assert created_user.username == user["username"]
    assert created_user.email == user["email"]
    assert created_user.first_name == user["first_name"]
    assert created_user.last_name == user["last_name"]
    assert created_user.is_superuser
    assert created_user.is_staff
