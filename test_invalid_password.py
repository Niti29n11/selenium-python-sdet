from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()

def test_invalid_cred():
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("abcdef")
    driver.find_element(By.ID, "login-button").click()
    message = driver.find_element(By.CSS_SELECTOR, "h3[data-test=error]").text
    time.sleep(2)
    print(message)
    assert message == "Epic sadface: Username and password do not match any user in this service"
    print("Test invalid password successfully")
    driver.quit()