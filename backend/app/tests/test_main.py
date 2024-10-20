import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from ..schemas.user import User


def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
