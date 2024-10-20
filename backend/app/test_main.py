import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from .dependencies import get_session
from .main import app


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


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
        ("invalid_email", "password123", "test2", 422, []),
    ],
)
def test_create_user(
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


# @pytest.mark.parametrize("skip,limit", [(0, 100), (10, 50)])
# def test_read_users(client, skip, limit):
#     response = client.get("/users/", params={"skip": skip, "limit": limit})
#     assert response.status_code == 200
#     assert len(response.json()) <= limit


# @pytest.mark.parametrize(
#     "user_id,expected_status_code", [(1, 200), (100, 404), (100, 404)]
# )
# def test_read_user(client, user_id, expected_status_code):
#     response = client.get(f"/users/{user_id}")
#     assert response.status_code == expected_status_code
