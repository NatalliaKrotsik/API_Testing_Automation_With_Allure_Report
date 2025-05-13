import pytest
import allure
from api.clients.auth_client import AuthClient

@allure.feature("Authentication")
@allure.story("Successful login")
@allure.severity("Critical")
@pytest.mark.api
def test_successful_login(config):
    client = AuthClient(config["api_base_url"])
    response = client.login("eve.holt@reqres.in", "cityslicka")

    with allure.step("Verify successful login"):
        assert response.status_code == 200
        assert "token" in response.json()

@allure.feature("Authentication")
@allure.story("Missing password")
def test_login_missing_password(config):
    client = AuthClient(config["api_base_url"])
    response = client.login("peter@klaven", "")

    with allure.step("Verify 400 error and error message"):
        assert response.status_code == 400
        assert "error" in response.json()
        assert response.json()["error"] == "Missing password"
