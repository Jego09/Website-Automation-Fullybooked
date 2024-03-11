from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class admin():
    def admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.Fullybookedonline.com/fbqdm1n")     

        username = self.driver.find_element(By.ID, "username")
        username.send_keys("carllimpiado")
        print("Entered Username")
        time.sleep(2)

        password = self.driver.find_element(By.ID, "login")
        password.send_keys("3DFE632B5D")
        print("Entered Password")
        time.sleep(2) 

        sign_in = self.driver.find_element(By.XPATH, "//*[@id='login-form']/fieldset/div[3]/div[1]/button/span")
        sign_in.click()
        time.sleep(10)
        print("Signed in")


if __name__ == "__main__":
    admin_login = admin()
    admin_login.admin_login()
        
