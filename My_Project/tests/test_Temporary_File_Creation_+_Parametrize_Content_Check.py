import pytest
import os

# 1. Fixture to create and delete temp file
@pytest.fixture
def temp_file():
    file_path = "temp_test_file.txt"
    with open(file_path, "w") as f:
        f.write("Temporary test data")  # 👈 Initial file content

    yield file_path  # 👈 Give control to test

    if os.path.exists(file_path):
        os.remove(file_path)

# 2. Parametrized test to validate file content
@pytest.mark.parametrize("expected_content, should_match", [
    ("Temporary test data", True),
    ("Wrong content", False),
    ("", False),
])
def test_temp_file_content(temp_file, expected_content, should_match):
    with open(temp_file, "r") as f:
        actual_content = f.read() 
    assert (actual_content == expected_content) == should_match

