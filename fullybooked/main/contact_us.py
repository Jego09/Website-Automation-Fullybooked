from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class contact_us():

    def __init__(self, driver):
        self.driver = driver
        
    def click_contact_us(self):

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
        print("Clicked Login Button")
        login_button.click()
        time.sleep(2)

        click_contact = self.driver.find_element(By.XPATH, "//*[@id='root']/div/footer/div[3]/div/div/div/div/div/div[2]/details[2]/ul/li[1]/a")
        click_contact.click()
        time.sleep(7)

if __name__ == "__main__":
    contact_click = contact_us()
    contact_click.click_contact_us() 
