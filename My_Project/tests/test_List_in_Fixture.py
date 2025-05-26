import pytest

@pytest.fixture
def my_list():
    my_list = []
    print("[Fixture] Providing empty list:", my_list)
    print(my_list)

    yield my_list

def test_1(my_list):
    my_list.append("A") 
    print("[Test 1] List after append:", my_list)
    assert my_list == ["A"] 

print("[Fixture] Providing empty list")    
def test_2(my_list):
    my_list.append("B") 
    print("[Test 2] List after append:", my_list)
    assert my_list == ["B"]