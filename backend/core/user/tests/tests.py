import pytest

from core.user.models import User
from core.user.tests.fixtures import data_user


@pytest.mark.django_db
def test_create_user():
    created_user = User.objects.create_user(**data_user)
    assert created_user.username == data_user["username"]
    assert created_user.email == data_user["email"]
    assert created_user.first_name == data_user["first_name"]
    assert created_user.last_name == data_user["last_name"]


@pytest.mark.django_db
def test_create_superuser():
    created_user = User.objects.create_superuser(**data_user)
    assert created_user.username == data_user["username"]
    assert created_user.email == data_user["email"]
    assert created_user.first_name == data_user["first_name"]
    assert created_user.last_name == data_user["last_name"]
    assert created_user.is_superuser
    assert created_user.is_staff
