from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

def test_login_page():
    driver.get("https://www.saucedemo.com")
    print(driver.title)
    print(driver.current_url)

    driver.find_element(By.CSS_SELECTOR, "input[id=user-name]").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    print("After login URL:", driver.current_url)
    print("Heading:", driver.find_element(By.CLASS_NAME, "app_logo").text)
    time.sleep(3)

    products= driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print("Product list is: ", len(products)) # 6 list of products
    print(driver.find_elements(By.ID, "nothing")) # No error 
    #driver.find_element(By.ID, "nothing") # NoSuchElementException
    driver.quit()





