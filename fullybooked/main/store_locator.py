from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class store_locator():
    def locator(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")        

        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "html-body")))
        time.sleep(2)

        login_register_button = self.driver.find_element(By.ID, "myAccount")
        login_register_button.click()
        print("Clicked Login/Register Button")
        time.sleep(2)

        username = self.driver.find_element(By.ID, "email")
        username.send_keys("btad@fullybookedonline.com")
        print("Entered Username")
        time.sleep(1)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("@HOsOCRmzkt4ngZ0YIaKj")
        print("Entered Password")
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section/header/nav/div[2]/div/div/div/form/div[4]/button")
        login_button.click()
        print("Clicked Login Button")
        time.sleep(3)

        locator_click = self.driver.find_element(By.XPATH, "//*[@id='root']/div/footer/div[3]/div/div/div/div/div/div[2]/details[1]/ul/li[7]/a")
        print("Clicked Live Chat Button")        
        locator_click.click()
        time.sleep(20)

if __name__ == "__main__":
    chat_live = store_locator()
    chat_live.locator()
        
