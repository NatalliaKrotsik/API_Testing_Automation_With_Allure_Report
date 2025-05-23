import pytest

# Fixture that will be overridden by parametrize
@pytest.fixture
def operation_func(request):
    return request.param

# Parametrized test with fixture + ids
@pytest.mark.parametrize("operation_func, x, y, expected", [
    (lambda x, y: x + y, 2, 3, 5),
    (lambda x, y: x - y, 5, 2, 3),
    (lambda x, y: x * y, 3, 4, 12),
], ids=["Addition", "Subtraction", "Multiplication"], indirect=["operation_func"])
def test_operations(operation_func, x, y, expected):
    result = operation_func(x, y)
    assert result == expected
