import pytest

from core.bank.models import Bank
from core.user.tests.fixtures import user_db


@pytest.mark.django_db
def test_create_bank(user_db):
    created_bank = Bank.objects.create(author=user_db, description="test")
    assert created_bank.author == user_db
    assert created_bank.description == "test"
