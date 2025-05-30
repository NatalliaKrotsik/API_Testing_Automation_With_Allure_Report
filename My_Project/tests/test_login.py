# test_login.py
def test_add_name(user_profile):
    user_profile["name"] = "Alice"
    assert "name" in user_profile
