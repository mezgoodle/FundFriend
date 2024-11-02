import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from ..dependencies import get_current_active_user, get_session
from ..main import app
from ..schemas import chat as chat_schema
from ..schemas import document as document_schema
from ..schemas import message as message_schema
from ..schemas import user as user_schema

# Створення тестової бази даних в пам'яті
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)


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
def client_fixture(session: Session, test_user: user_schema.User):
    def get_session_override():
        return session

    def get_current_active_user_override():
        return test_user

    app.dependency_overrides[get_session] = get_session_override
    app.dependency_overrides[get_current_active_user] = (
        get_current_active_user_override
    )
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(session: Session):
    user_data = user_schema.UserCreate(
        email="existing_user@example.com",
        password="password123",
        name="Existing User",
    )
    user_data.password = None
    user = user_schema.User(
        **user_data.model_dump(), hashed_password="password123"
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@pytest.fixture
def test_chat(session: Session, test_user: user_schema.User):
    chat_data = chat_schema.ChatCreate(
        title="Test Chat",
        description="Test Chat Description",
    )
    chat = chat_schema.Chat(
        **chat_data.model_dump(),
        owner_id=test_user.id,
    )
    session.add(chat)
    session.commit()
    session.refresh(chat)
    return chat


@pytest.fixture
def test_document(session: Session, test_user: user_schema.User):
    document_data = document_schema.DocumentCreate(
        name="Test Document",
        bucket_url="https://example.com/test.pdf",
        owner_id=test_user.id,
    )
    document = document_schema.Document(**document_data.model_dump())
    session.add(document)
    session.commit()
    session.refresh(document)
    return document


@pytest.fixture
def test_message(
    session: Session, test_user: user_schema.User, test_chat: chat_schema.Chat
):
    message_data = message_schema.MessageCreate(
        owner_id=test_user.id,
        chat_id=test_chat.id,
        text="Hello, World!",
    )
    message = message_schema.Message(**message_data.model_dump())
    session.add(message)
    session.commit()
    session.refresh(message)
    return message
