from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1280,800")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)

    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys("I am so happy today!")

    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()
    time.sleep(2)

    driver.save_screenshot("6b_deployment_test.png")
    print("Screenshot saved to 6b_deployment_test.png")
finally:
    driver.quit()
