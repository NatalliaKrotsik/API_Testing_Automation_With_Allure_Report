import pytest
import allure


@allure.feature("String Transformation")
@allure.story("Apply different transformation functions")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify string transformation functions produce expected output")
@allure.description("""
This test verifies the correctness of basic string transformation operations:
- lowercasing,
- trimming spaces,
- replacing specific substrings.
""")
@pytest.mark.parametrize("transform_func, input_str, expected", [
    (lambda s: s.lower(), "HAVE A GOOD DAY", "have a good day"),
    (lambda s: s.strip(), " book ", "book"),
    (lambda s: s.replace("tool", "case"), "test_tool", "test_case"),
], ids=["Lowercase", "Remove spaces", "Replace 'tool' with 'case'"])
def test_string_transform(transform_func, input_str, expected):
    with allure.step(f"Transforming '{input_str}'"):
        result = transform_func(input_str)
        assert result == expected, f"Expected '{expected}', got '{result}'"
