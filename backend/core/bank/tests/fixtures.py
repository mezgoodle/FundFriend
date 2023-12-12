import pytest

from core.bank.models import Bank
from core.user.tests.fixtures import user_db


@pytest.fixture
def bank_db(user_db):
    return Bank.objects.create(author=user_db, description="test")
