import pytest
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


client = TestClient(app)


@pytest.mark.parametrize(
    "email,password,expected_status_code",
    [
        ("test@example.com", "password123", 201),
        ("test@example.com", "password123", 400),
        ("invalid_email", "password123", 422),
    ],
)
def test_create_user(email, password, expected_status_code):
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == expected_status_code


@pytest.mark.parametrize("skip,limit", [(0, 100), (10, 50)])
def test_read_users(skip, limit):
    response = client.get("/users/", params={"skip": skip, "limit": limit})
    assert response.status_code == 200
    assert len(response.json()) <= limit


@pytest.mark.parametrize(
    "user_id,expected_status_code", [(1, 200), (100, 404), (100, 404)]
)
def test_read_user(user_id, expected_status_code):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "user_id,title,description",
    [(1, "Item 1", "Description 1"), (2, "Item 2", "Description 2")],
)
def test_create_item_for_user(user_id, title, description):
    response = client.post(
        f"/users/{user_id}/items/",
        json={"title": title, "description": description},
    )
    assert response.status_code == 201


@pytest.mark.parametrize("skip,limit", [(0, 100), (10, 50)])
def test_read_items(skip, limit):
    response = client.get("/items/", params={"skip": skip, "limit": limit})
    assert response.status_code == 200
    assert len(response.json()) <= limit
