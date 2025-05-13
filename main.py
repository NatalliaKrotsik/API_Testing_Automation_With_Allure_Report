import main
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@main.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
