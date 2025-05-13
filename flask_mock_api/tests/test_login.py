import requests
import pytest
import allure

@allure.feature("Login API")
@allure.story("Valid login returns 200")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test valid login with correct credentials")
@allure.description("This test validates the login endpoint for successful login.")

@pytest.mark.parametrize("email, password, expected_status", [
    ("eve.holt@reqres.in", "pistol", 200),
    ("eve.holt@reqres.in", "", 400),
    ("", "pistol", 400),
    ("wrong@example.com", "wrong", 400),
])
def test_login(base_url, email, password, expected_status):
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(f"{base_url}/login", json=payload)

    assert response.status_code == expected_status
    if response.status_code == 200:
        assert "token" in response.json()
    else:
        assert "error" in response.json()
