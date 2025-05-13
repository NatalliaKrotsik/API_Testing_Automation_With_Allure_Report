import requests
import pytest

def test_get_existing_user(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

@pytest.mark.parametrize("user_id", [999, 0])
def test_get_nonexistent_user(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404
    assert "error" in response.json()
