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


def test_read_messages_by_user(client, test_user, test_message):
    response = client.get(f"/messages/user/{test_user.id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    message = response.json()[0]
    assert message["id"] == test_message.id
    assert message["owner_id"] == test_message.owner_id


def test_read_messages_by_chat(client, test_chat, test_message, test_user):
    response = client.get(f"/messages/chat/{test_chat.id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    message = response.json()[0]
    assert message["id"] == test_message.id
    assert message["chat_id"] == test_message.chat_id
    assert message["owner_id"] == test_user.id
