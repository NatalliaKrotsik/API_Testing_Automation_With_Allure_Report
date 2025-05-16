import pytest
import os

@pytest.fixture
def temp_file():
    file_path = "test_data.txt"
    
    # 🔧 Setup
    with open(file_path, "w") as f:
        f.write("Temporary test content")
    print("[Fixture] File created")

    yield file_path  # 👈 Give control to the test

    # 🧹 Teardown
    if os.path.exists(file_path):
        os.remove(file_path)
        print("[Fixture] File deleted")

def test_read_temp_file(temp_file):
    print("[Test] Reading file content")
    with open(temp_file, "r") as f:
        content = f.read()
    
    assert content == "Temporary test content"
