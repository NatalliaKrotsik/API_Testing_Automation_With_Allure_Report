# conftest.py
import pytest

@pytest.fixture
def user_profile():
    profile = {}
    print("[Fixture] Shared user profile")
    return profile
