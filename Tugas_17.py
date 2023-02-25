import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_a_success_login(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME, "title").text
        self.assertIn('PRODUCTS', response_data)

    def test_a_failed_login(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("admin")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("password")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_message = driver.find_element(By.TAG_NAME, "h3").text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_message)

    def test_a_failed_login_with_empty_email_and_password(self):
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_message = driver.find_element(By.TAG_NAME, "h3").text
        self.assertIn('Epic sadface: Username is required', response_message)

    



    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()