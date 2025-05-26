import pytest
import allure


@allure.feature("Database Connection")
@allure.story("Simulate DB session with a fixture")
@pytest.fixture
def db_connection():
    with allure.step("Establishing test database connection"):
        print("[Fixture] Connecting to database")
        connection = {"status": "connected", "db": "TestDB"}
        yield connection
        print("[Fixture] Closing database connection")


@allure.feature("Database Connection")
@allure.story("Verify connection status")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test DB connection status is 'connected'")
@allure.description("This test ensures that the database connection status is established correctly.")
def test_db_status(db_connection):
    with allure.step("Checking connection status"):
        print("[Test_1] Check status")
        assert db_connection["db"] == "TestDB"
