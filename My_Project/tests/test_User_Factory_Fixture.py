import pytest
from faker import Faker

fake = Faker()

@pytest.fixture(scope="function")
def fake_user():
    print("Setting up data")
    return  {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=10)
    }
def test_one(fake_user):
    print("Running test_one")
    print(fake_user)
    assert "@" in fake_user["email"]
    assert len(fake_user["password"]) >= 8

def test_two(fake_user):
    print("Running test_two")
    print(fake_user)
    assert isinstance(fake_user["name"], str)
    assert len(fake_user["name"]) > 0
