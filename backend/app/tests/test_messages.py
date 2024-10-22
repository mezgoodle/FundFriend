import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from ..schemas.message import Message


@pytest.mark.parametrize(
    "message_id,expected_status_code", [(1, 200), (100, 404)]
)
def test_read_message(client, message_id, expected_status_code, test_message):
    response = client.get(f"/messages/{message_id}")
    assert response.status_code == expected_status_code


def test_create_message(client, test_user, test_chat):
    message_data = {
        "text": "Hello, World!",
        "owner_id": test_user.id,
        "chat_id": test_chat.id,
    }
    response = client.post("/messages/", json=message_data)
    data = response.json()

    assert response.status_code == 201
    assert data["text"] == "Hello, World!"
    assert data["owner_id"] == test_user.id
    assert data["chat_id"] == test_chat.id
    assert "id" in data


def test_update_message(test_message, client):
    message_id = test_message.id
    response = client.put(
        f"/messages/{message_id}", json={"text": "Updated Message"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["text"] == "Updated Message"
    assert data["id"] == message_id


def test_delete_message(test_message, session: Session, client: TestClient):
    message_id = test_message.id
    response = client.delete(f"/messages/{message_id}")
    assert response.status_code == 204
    assert session.get(Message, message_id) is None
