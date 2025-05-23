import pytest

@pytest.mark.parametrize("transform_func, input_str, expected", [
    (lambda s: s.lower(), "HAVE A GOOD DAY", "have a good day"),
    (lambda s: s.strip(), " book ", "book"),
    (lambda s: s.replace("tool", "case"), "test_tool", "test_case"),
], ids=["Lowercase", "Remove spaces", "Replace 'tool' with 'case'"])

def test_string_transform(transform_func, input_str, expected):
    assert transform_func(input_str) == expected