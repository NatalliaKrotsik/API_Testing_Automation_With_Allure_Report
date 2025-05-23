import pytest

@pytest.fixture
def my_list():
    my_list = []
    print(my_list)
def test_1(my_list):
    my_list.append("A") 
    assert "A" in my_list 
    
def test_2(my_list):
    my_list.append("B") 
    assert "A, B" in my_list