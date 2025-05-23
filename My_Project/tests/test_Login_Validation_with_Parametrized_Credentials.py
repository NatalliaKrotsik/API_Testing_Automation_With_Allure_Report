import pytest

# 1. Fixture: Define valid login credentials
@pytest.fixture
def user_credential():
    return {"username":"admin","password":"secret123"}

# 2. Parametrize: Define test cases with (username, password, expected_result)
@pytest.mark.parametrize("username, password, expected_result", [
    ("admin", "secret123", True),
    ("guest", "nopass", False),
    ("admin", "wrongpass", False),
])

# 3. Test function: Use the fixture and assert login success/failure

def test_user_credential(username, password, expected_result, user_credential):
    creds = user_credential
    is_valid = username == creds["username"] and password == creds["password"]
    assert is_valid == expected_result