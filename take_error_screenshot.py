from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1280,400")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)

    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()
    time.sleep(2)

    driver.save_screenshot("7c_error_handling_interface.png")
    print("Error handling screenshot saved to 7c_error_handling_interface.png")
finally:
    driver.quit()
