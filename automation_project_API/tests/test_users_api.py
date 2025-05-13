import pytest
import allure
from api.clients.user_client import UserClient

@allure.epic("User Management API")
@allure.feature("GET /users/{id}")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that user with ID 1 can be fetched successfully")
def test_get_user_by_id(config):
    client = UserClient(config["api_base_url"])
    response = client.get_user(1)

    with allure.step("Check response code and user data"):
        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert response.json()["username"] == "Bret"

# ✅ Add this test below (in the same file)
@pytest.mark.parametrize("user_id, expected_username", [
    (1, "Bret"),
    (2, "Antonette"),
    (3, "Samantha")
])
@allure.feature("GET /users/{id} with multiple inputs")
@allure.title("Verify different users by ID and username")
def test_get_user_parametrized(config, user_id, expected_username):
    client = UserClient(config["api_base_url"])
    response = client.get_user(user_id)

    with allure.step(f"Validate user ID: {user_id} and username: {expected_username}"):
        assert response.status_code == 200
        assert response.json()["username"] == expected_username

@allure.feature("Negative Test - GET /users/{invalid_id}")
@pytest.mark.parametrize("invalid_id", [0, 9999, "abc"])
def test_get_nonexistent_user(config, invalid_id):
    client = UserClient(config["api_base_url"])
    response = client.get_user(invalid_id)

    with allure.step(f"Verify 404 for invalid user ID: {invalid_id}"):
        assert response.status_code == 404
        assert response.text == "{}"  # JSONPlaceholder returns an empty object
