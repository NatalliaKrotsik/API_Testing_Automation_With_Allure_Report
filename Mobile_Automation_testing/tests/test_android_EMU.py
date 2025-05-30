from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "emulator-5554"
options.appPackage = "com.android.calculator2"
options.appActivity = ".Calculator"
options.automationName = "UiAutomator2"
options.noReset = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(2)

driver.find_element("id", "com.android.calculator2:id/digit_2").click()
driver.find_element("id", "com.android.calculator2:id/op_add").click()
driver.find_element("id", "com.android.calculator2:id/digit_2").click()
driver.find_element("id", "com.android.calculator2:id/eq").click()

result = driver.find_element("id", "com.android.calculator2:id/result").text
assert result == "4", f"Expected 4 but got {result}"

print("✅ Test passed: 2 + 2 = 4")

driver.quit()
