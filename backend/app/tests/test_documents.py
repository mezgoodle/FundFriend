import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from ..schemas.document import Document


@pytest.mark.parametrize(
    "document_id,expected_status_code", [(1, 200), (100, 404)]
)
def test_read_document(
    client, document_id, expected_status_code, test_document
):
    response = client.get(f"/documents/{document_id}")
    assert response.status_code == expected_status_code


def test_create_document(client, test_user):
    file_content = b"Test file content"
    files = {"file": ("test.pdf", file_content, "application/pdf")}
    response = client.post("/documents/", files=files)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "test.pdf"
    assert data["owner_id"] == test_user.id
    assert data["bucket_url"] == "/documents/test.pdf"
    assert "id" in data


def test_update_document(test_document, client):
    document_id = test_document.id
    response = client.put(
        f"/documents/{document_id}", json={"name": "Updated Document"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Updated Document"
    assert data["id"] == document_id


def test_delete_document(test_document, session: Session, client: TestClient):
    document_id = test_document.id
    response = client.delete(f"/documents/{document_id}")
    assert response.status_code == 204
    assert session.get(Document, document_id) is None


def test_read_documents_by_user(client, test_user, test_document):
    response = client.get(f"/documents/user/{test_user.id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    document = response.json()[0]
    assert document["id"] == test_document.id
    assert document["owner_id"] == test_document.owner_id
