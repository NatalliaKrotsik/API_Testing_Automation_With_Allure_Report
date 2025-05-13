# utils.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging

def fill_input_field(driver, by, value, text):
    try:
        input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
        input_field.send_keys(text)
        logging.info(f"Filled input field with {by} = {value} with text '{text}'")
    except NoSuchElementException:
        logging.error(f"Input field with {by} = {value} not found")