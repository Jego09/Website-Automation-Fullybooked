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
        click_contact = self.driver.find_element(By.XPATH, "//*[@id='root']/div/footer/div[3]/div/div/div/div/div/div[2]/details[2]/ul/li[1]/a")
        click_contact.click()
        time.sleep(7)

if __name__ == "__main__":
    contact_click = contact_us()
    contact_click.click_contact_us() 
