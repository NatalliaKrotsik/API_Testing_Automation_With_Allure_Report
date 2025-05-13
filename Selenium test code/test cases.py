# test_registration.py
import logging
from selenium.webdriver.common.by import By
from utils import fill_input_field

# Configure logging
logging.basicConfig(level=logging.INFO)

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