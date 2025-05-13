from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch the browser and open the website
driver = webdriver.Chrome()  # or Edge(), Firefox()
driver.get("https://testdrive.andersenlab.com/")  # Replace with the actual login page URL
driver.maximize_window()

wait = WebDriverWait(driver, 10)
# CSS Selector
continue_button = driver.find_element(By.CSS_SELECTOR, "a#go_to_step_2")
continue_button.click()

continue_button = driver.find_element(By.CSS_SELECTOR, "select#engine")
continue_button.click()

continue_button = driver.find_element(By.CSS_SELECTOR, "select#engine > option")
continue_button.click()

continue_button = driver.find_element(By.CSS_SELECTOR, "a#go_to_step_3")
continue_button.click()

last_name_input = wait.until(EC.visibility_of_element_located((By.ID, "form_last_name")))
last_name_input.send_keys("Doe")

first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "form_first_name")))
first_name_input.send_keys("John")

Age_input = wait.until(EC.visibility_of_element_located((By.ID, "form_age")))
Age_input.send_keys("23")

Phone_number_input = wait.until(EC.visibility_of_element_located((By.ID, "form_phone")))
Phone_number_input.send_keys("234345456")

continue_button = driver.find_element(By.CSS_SELECTOR, "a#go_to_step_4")
continue_button.click()

continue_button = driver.find_element(By.CSS_SELECTOR, "a#finish")
continue_button.click()



input("Press Enter to close the browser...")
# Step 6: Close the browser
driver.quit()

