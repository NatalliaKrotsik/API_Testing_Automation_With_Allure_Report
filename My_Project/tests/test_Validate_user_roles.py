import pytest

# Access check function
def has_access(role):
    return role in ["admin", "editor"]

# Parametrized test with custom IDs
@pytest.mark.parametrize("role, expected", [
    ("admin", True),
    ("editor", True),
    ("guest", False),
], ids=["AdminAccess", "EditorAccess", "GuestDenied"])
def test_user_access(role, expected):
    result = has_access(role)
    assert result == expected
