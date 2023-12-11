import pytest
from rest_framework import status


@pytest.fixture
def user_data():
    return {
        "username": "johndoe",
        "email": "johndoe@yopmail.com",
        "password": "test_password",
        "first_name": "John",
        "last_name": "Doe",
    }


class TestAuthenticationViewSet:
    endpoint = "/api/auth/"

    @pytest.mark.django_db
    def test_register(self, client, user_data):
        response = client.post(self.endpoint + "register/", user_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["user"]["email"] == user_data["email"]
        assert response.data["user"]["first_name"] == user_data["first_name"]
        assert response.data["user"]["last_name"] == user_data["last_name"]
        assert response.data["access"] is not None
        assert response.data["refresh"] is not None

    @pytest.mark.django_db
    def test_login(self, client, user_data):
        register_response = client.post(self.endpoint + "register/", user_data)
        assert register_response.status_code == status.HTTP_201_CREATED
        data = {
            "email": user_data["email"],
            "password": user_data["password"],
        }
        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"] is not None
        assert response.data["refresh"] is not None
        assert response.data["user"]["email"] == data["email"]

    @pytest.mark.django_db
    def test_refresh(self, client, user_data):
        _ = client.post(self.endpoint + "register/", user_data)
        data = {"email": user_data["email"], "password": user_data["password"]}
        response = client.post(self.endpoint + "login/", data)

        assert response.status_code == status.HTTP_200_OK

        data_refresh = {"refresh": response.data["refresh"]}

        response = client.post(self.endpoint + "refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
