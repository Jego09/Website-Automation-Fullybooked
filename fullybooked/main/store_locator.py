from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class store_locator():

    def __init__(self, driver):
        self.driver = driver
    
    def locator(self):
        locator_click = self.driver.find_element(By.XPATH, "//*[@id='root']/div/footer/div[3]/div/div/div/div/div/div[2]/details[1]/ul/li[7]/a")
        print("Clicked Store Locator Button")        
        locator_click.click()
        time.sleep(20)

if __name__ == "__main__":
    chat_live = store_locator()
    chat_live.locator()
        
