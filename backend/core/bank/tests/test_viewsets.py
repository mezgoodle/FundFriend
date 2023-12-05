import pytest
from rest_framework import status

from core.bank.tests.fixtures import bank_db
from core.user.tests.fixtures import user_db


class TestBankViewSet:
    endpoint = "/api/banks/"

    @pytest.mark.django_db
    def test_list(self, client, user_db, bank_db):
        assert bank_db is not None
        client.force_authenticate(user=user_db)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    @pytest.mark.django_db
    def test_retrieve(self, client, bank_db):
        response = client.get(f"{self.endpoint}{bank_db.public_id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == bank_db.public_id.hex
        assert response.data["description"] == bank_db.description
        assert response.data["author"]["id"] == bank_db.author.public_id.hex

    @pytest.mark.django_db
    def test_create(self, client, user_db):
        client.force_authenticate(user=user_db)
        response = client.post(
            self.endpoint, {"author": user_db.public_id, "description": "test"}
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["description"] == "test"
        assert response.data["author"]["id"] == user_db.public_id.hex

    @pytest.mark.django_db
    def test_update(self, client, bank_db):
        client.force_authenticate(user=bank_db.author)
        response = client.patch(
            f"{self.endpoint}{bank_db.public_id}/", {"description": "test"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["description"] == "test"
        assert response.data["author"]["id"] == bank_db.author.public_id.hex

    @pytest.mark.django_db
    def test_delete(self, client, bank_db):
        client.force_authenticate(user=bank_db.author)
        response = client.delete(f"{self.endpoint}{bank_db.public_id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_create_anonymous(self, client, user_db):
        response = client.post(
            self.endpoint, {"author": user_db.public_id, "description": "test"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_update_anonymous(self, client, bank_db):
        response = client.patch(
            f"{self.endpoint}{bank_db.public_id}/", {"description": "test"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_delete_anonymous(self, client, bank_db):
        response = client.delete(f"{self.endpoint}{bank_db.public_id}/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
