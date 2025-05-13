# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # or Edge(), Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()