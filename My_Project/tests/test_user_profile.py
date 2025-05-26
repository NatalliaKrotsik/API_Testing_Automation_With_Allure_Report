import pytest

@pytest.fixture
def user_profile():
    profile = {}
    print("[Fixture] Providing empty user profile:", profile)
    yield profile

def test_add_name(user_profile):
    user_profile["name"] = "Alice"
    print("[Test 1] Profile after adding name:", user_profile)
    assert user_profile["name"] == "Alice"

def test_add_role(user_profile):
    user_profile["role"] = "QA Engineer"
    print("[Test 2] Profile after adding role:", user_profile)
    assert user_profile["role"] == "QA Engineer"
