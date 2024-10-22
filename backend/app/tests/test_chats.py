import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from ..schemas.chat import Chat


@pytest.mark.parametrize(
    "chat_id,expected_status_code", [(1, 200), (100, 404)]
)
def test_read_chat(client, chat_id, expected_status_code, test_chat):
    response = client.get(f"/chats/{chat_id}")
    assert response.status_code == expected_status_code


def test_create_chat(client, test_user):
    chat_data = {"title": "New Chat", "owner_id": test_user.id}
    response = client.post("/chats/", json=chat_data)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "New Chat"
    assert data["owner_id"] == test_user.id
    assert "id" in data


def test_update_chat(test_chat, client):
    chat_id = test_chat.id
    response = client.put(f"/chats/{chat_id}", json={"title": "Updated Chat"})
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Updated Chat"
    assert data["id"] == chat_id


def test_delete_chat(test_chat, session: Session, client: TestClient):
    chat_id = test_chat.id

    response = client.delete(f"/chats/{chat_id}")

    chat_in_db = session.get(Chat, chat_id)

    assert response.status_code == 200
    assert chat_in_db is None
