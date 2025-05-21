import pytest

@pytest.fixture
def db_connection():
    print("[Fixture] Connecting to database")
    connection = {"status": "connected", "db": "TestDB"}

    yield connection

    print("[Fixture] Closing database connection")

def test_db_status(db_connection):
    print("[Test_1] Check status")
    assert db_connection["status"] == "connected"

def test_db_name(db_connection):
    print("[Test_2] Check database name")
    assert db_connection["db"] == "TestDB"