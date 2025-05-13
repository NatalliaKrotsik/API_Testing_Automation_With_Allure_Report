
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # or Edge(), Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def fill_input_field(driver, by, value, text):
    try:
        input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
        input_field.send_keys(text)
        logging.info(f"Filled input field with {by} = {value} with text '{text}'")
    except NoSuchElementException:
        logging.error(f"Input field with {by} = {value} not found")

def test_selenium_workflow(driver):
    driver.get("https://testdrive.andersenlab.com/")
    logging.info("Navigated to https://testdrive.andersenlab.com/")

    driver.find_element(By.CSS_SELECTOR, "a#go_to_step_2").click()
    driver.find_element(By.CSS_SELECTOR, "select#engine").click()
    driver.find_element(By.CSS_SELECTOR, "select#engine > option").click()
    driver.find_element(By.CSS_SELECTOR, "a#go_to_step_3").click()

    fill_input_field(driver, By.ID, "form_last_name", "Doe")
    fill_input_field(driver, By.ID, "form_first_name", "John")
    fill_input_field(driver, By.ID, "form_age", "23")
    fill_input_field(driver, By.ID, "form_phone", "234345456")

    driver.find_element(By.CSS_SELECTOR, "a#go_to_step_4").click()
    driver.find_element(By.CSS_SELECTOR, "a#finish").click()
