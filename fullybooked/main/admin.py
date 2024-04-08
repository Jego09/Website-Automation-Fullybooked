from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from elements import AdminLocators

class admin():
    def admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.Fullybookedonline.com/fbqdm1n")     

        username = self.driver.find_element(By.ID, AdminLocators.USERNAME)
        username.send_keys(AdminLocators.USERNAME_INPUT)
        print("Entered Username")
        time.sleep(2)

        password = self.driver.find_element(By.ID, AdminLocators.PASSWORD)
        password.send_keys(AdminLocators.PASSWORD_INPUT)
        print("Entered Password")
        time.sleep(2) 

        sign_in = self.driver.find_element(By.XPATH, AdminLocators.SIGN_IN_BUTTON)
        sign_in.click()
        time.sleep(10)
        print("Signed in")


if __name__ == "__main__":
    admin_login = admin()
    admin_login.admin_login()
        
