import pytest

@pytest.fixture(scope="function")
def login_session():
    print("[Fixture] Session started\n")
    
    session = {"token": "abc123", "user": "qa_engineer"}
    yield session

    print("[Fixture] Session ended")

def test_token_exists(login_session):
    print("[Test_1] Check token exists")
    assert "token" in login_session 

def test_user_is_qa_engineer(login_session):
    print("[Test_2] Check user role")