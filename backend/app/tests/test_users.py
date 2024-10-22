import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from ..schemas.user import User


@pytest.mark.parametrize(
    "email,password,name,expected_status_code,fields_to_assert",
    [
        (
            "test@example.com",
            "password123",
            "test",
            201,
            ["email", "name", "is_active", "id"],
        ),
        ("existing_user@example.com", "password123", "Existing User", 400, []),
        ("invalid_email", "password123", "test2", 422, []),
    ],
)
def test_create_user(
    test_user: User,
    client: TestClient,
    email: str,
    password: str,
    name: str,
    expected_status_code: int,
    fields_to_assert: list,
):
    response = client.post(
        "/users/",
        json={"email": email, "password": password, "name": name},
    )
    assert response.status_code == expected_status_code
    data = response.json()
    for field in fields_to_assert:
        assert field in data
        assert data[field] is not None


@pytest.mark.parametrize("offset,limit", [(0, 100), (10, 50)])
def test_read_users(client, offset, limit):
    response = client.get("/users/", params={"offset": offset, "limit": limit})
    assert response.status_code == 200
    assert len(response.json()) <= limit


@pytest.mark.parametrize(
    "user_id,expected_status_code", [(1, 200), (100, 404), (100, 404)]
)
def test_read_user(test_user, client, user_id, expected_status_code):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == expected_status_code


def test_update_user(test_user, client):
    user_id = test_user.id

    response = client.put(f"/users/{user_id}", json={"name": "Deadpuddle"})
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Deadpuddle"
    assert data["id"] == user_id


def test_delete_user(test_user, session: Session, client: TestClient):
    user_id = test_user.id

    response = client.delete(f"/users/{user_id}")

    user_in_db = session.get(User, user_id)

    assert response.status_code == 200

    assert user_in_db is None
