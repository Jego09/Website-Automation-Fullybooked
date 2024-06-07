from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import *
from elements import *
import os

wait_sec = 10

class SortBy:

    def __init__(self, driver):

        self.driver = driver
    
    def sort_newest(self):

        sort_by = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='category-sort_wrapper']/div")) # Sort By dropdown box xpath
        )
        sort_by.click()

        sort = self.driver.find_element(By.XPATH, SortByLocators.NEWEST)
        sort.click()        


class PageClicker:

    def __init__(self, driver):
        self.driver = driver
        self.page_number = 1
        self.max_page = 10
    # def click_next_page(self):

    #     while self.page_number <= self.max_page:

    #         try:

    #             element = self.driver.find_element(By.XPATH, NotificationLocators.NOTIF_GENERAL)
    #         #     element = WebDriverWait(self.driver, 10).until(
    #         #     EC.visibility_of_element_located((By.XPATH, NotificationLocators.NOTIF_GENERAL))
    #         # )
    #             if element.is_displayed():
    #             # if "Error Product Fetching!" in element.text:

    #                 self.driver.save_screenshot(f"D:\screenshot\error_product {self.page_number}.png")

    #                 print("SS Triggered")
                
    #             # self.driver.implicitly_wait(10)
            
    #         except NoSuchElementException:
                
    #             nested_try = True

    #             while nested_try:

    #                 try:

    #                     page_str = f"Page {self.page_number}"

    #                     page = WebDriverWait(self.driver, 10).until(
    #                         EC.element_to_be_clickable((By.XPATH, f'//a[@aria-label="{page_str}"]')))
    #                     page.click()
    #                     # element = self.driver.find_element(By.XPATH, f'//a[@aria-label="{page_str}"]')
    #                     # if element.is_displayed():
    #                     #     element.click()

    #                     print(f"Clicked page {self.page_number}")

    #                     self.page_number += 1

    #                     self.driver.implicitly_wait(10)
 
    #                 except NoSuchElementException:
    #                     print("1NoSuchElementException: Either Last page reached or Element does not load")
    #                     nested_try = False
                        
                        
    #                 except TimeoutException:
    #                     print("1TimeoutException: Either Last page reached or Element does not load")
    #                     nested_try = False
                        

    #                 except InvalidSessionIdException:
    #                     print("1InvalidSessionIdException: Either Last page reached or Browser does not load")
                        
                    
    #         except InvalidSessionIdException:
    #             print("2InvalidSessionIdException: Either Last page reached or Browser does not load")

        
    #     self.driver.quit()
            

    def click_next_page(self):
            
            try:
                
                errors =[TimeoutException]

                while self.page_number <= self.max_page:

                    page_str = f"Page {self.page_number}"

                    element = WebDriverWait(self.driver, 10, ignored_exceptions=errors).until(
                        EC.visibility_of_element_located((By.XPATH, f'//a[@aria-label="{page_str}"]')))
                    element.click()

                    print(f"Clicked page {self.page_number}")

                    self.page_number += 1
                    
            except TimeoutException:
                print("TimeoutException: Either Last page reached or Browser does not load")
    

