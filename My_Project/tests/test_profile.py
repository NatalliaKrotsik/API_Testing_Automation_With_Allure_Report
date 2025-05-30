# test_profile.py
def test_add_role(user_profile):
    user_profile["role"] = "QA Engineer"
    assert user_profile["role"] == "QA Engineer"
