from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import *
from elements import *

wait_sec = 10

class SortBy:

    def __init__(self, driver):

        self.driver = driver
    
    def sort_newest(self):

        sort_newest = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='category-sort_wrapper']/div"))
        )
        sort_newest.click()

        newest = self.driver.find_element(By.XPATH, SortByLocators.LOW_TO_HIGH)
        newest.click()        


class PageClicker:
    def __init__(self, driver):

        self.driver = driver
        self.page_number = 1

    def click_next_page(self):
        page_str = f"Page {self.page_number}"

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//a[@aria-label="{page_str}"]')))
        element.click()
        print(f"Clicked page {self.page_number}")

        self.page_number += 1