import pytest

from core.bank.tests.fixtures import bank_db
from core.document.models import Document
from core.user.tests.fixtures import user_db


@pytest.mark.django_db
def test_create_document(user_db, bank_db):
    created_document = Document.objects.create(
        author=user_db, title="test", text="test", bank=bank_db
    )
    assert created_document.author == user_db
    assert created_document.title == "test"
    assert created_document.text == "test"
    assert created_document.bank == bank_db
