from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginCustomer:

    def login(self):

        login_register_button = self.driver.find_element(By.ID, "myAccount")
        login_register_button.click()
        print("Clicked Login/Register Button")
        time.sleep(5)

        username = self.driver.find_element(By.ID, "email")
        username.send_keys("btad@fullybookedonline.com")
        print("Entered Username")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("@HOsOCRmzkt4ngZ0YIaKj")
        print("Entered Password")

        login_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section/header/nav/div[2]/div/div/div/form/div[4]/button")
        print("Clicked Login Button")
        login_button.click()
        time.sleep(2)

if __name__ == '__main__':
    login_instance = LoginCustomer()
    login_instance.login()
