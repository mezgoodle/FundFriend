import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database import Base
from .main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


@pytest.fixture(scope="session", autouse=True)
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


# Фікстура для клієнта FastAPI
@pytest.fixture(scope="module")
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.parametrize(
    "email,password,expected_status_code",
    [
        ("test@example.com", "password123", 201),
        ("test@example.com", "password123", 400),
        ("invalid_email", "password123", 422),
    ],
)
def test_create_user(client, email, password, expected_status_code):
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == expected_status_code


@pytest.mark.parametrize("skip,limit", [(0, 100), (10, 50)])
def test_read_users(client, skip, limit):
    response = client.get("/users/", params={"skip": skip, "limit": limit})
    assert response.status_code == 200
    assert len(response.json()) <= limit


@pytest.mark.parametrize(
    "user_id,expected_status_code", [(1, 200), (100, 404), (100, 404)]
)
def test_read_user(client, user_id, expected_status_code):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "user_id,title,description",
    [(1, "Item 1", "Description 1"), (2, "Item 2", "Description 2")],
)
def test_create_item_for_user(client, user_id, title, description):
    response = client.post(
        f"/users/{user_id}/items/",
        json={"title": title, "description": description},
    )
    assert response.status_code == 201


@pytest.mark.parametrize("skip,limit", [(0, 100), (10, 50)])
def test_read_items(client, skip, limit):
    response = client.get("/items/", params={"skip": skip, "limit": limit})
    assert response.status_code == 200
    assert len(response.json()) <= limit
