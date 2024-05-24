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

        sort_newest = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='category-sort_wrapper']/div"))
        )
        sort_newest.click()

        newest = self.driver.find_element(By.XPATH, SortByLocators.NEWEST)
        newest.click()        


class PageClicker:
    
    def __init__(self, driver):

        self.driver = driver
        self.page_number = 1
        self.max_page = 10
        self.screenshot_folder = r"D:\Python Projects\main\Jego-event-notes\fullybooked\Error Fetching Found"

    def click_next_page(self):
        
        page_str = f"Page {self.page_number}"

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//a[@aria-label="{page_str}"]')))
        element.click()
        print(f"Clicked page {self.page_number}")

        # while self.page_number <= self.max_page: // If max page limit is needed.
        self.page_number += 1

    # def errorFetch(self):
    #     # Create folder if it doesn't exist
    #     # if not os.path.exists(self.screenshot_folder):
    #     #     os.makedirs(self.screenshot_folder)
        
    #     # Define the screenshot file path
    #     page_str = f"Page_{self.page_number}.png"
    #     screenshot_path = os.path.join(self.screenshot_folder, page_str)

    #     error_elements = self.driver.find_element(By.XPATH, NotificationLocators.ERROR_FETCHING)
    #     if error_elements:
    #         # Save the screenshot using the driver object
    #         self.driver.save_screenshot(screenshot_path)

# class ErrorFetching:

#     def __init__(self, driver):
#         self.driver = driver
#         self.page_number = 1
#         self.screenshot_folder = r"D:\Python Projects\main\Jego-event-notes\fullybooked\Error Fetching Found"

#     def errorFetch(self):
#         # Create folder if it doesn't exist
#         if not os.path.exists(self.screenshot_folder):
#             os.makedirs(self.screenshot_folder)
        
#         # Define the screenshot file path
#         page_str = f"Page_{self.page_number}.png"
#         screenshot_path = os.path.join(self.screenshot_folder, page_str)

#         error_elements = self.driver.find_element(By.XPATH, NotificationLocators.ERROR_FETCHING)
#         if error_elements:
#             # Save the screenshot using the driver object
#             self.driver.save_screenshot(screenshot_path)

# class PageClicker:
#     def __init__(self, driver):
#         self.driver = driver
#         self.page_number = 1
#         self.max_page = 10
#         self.screenshot_folder = r"D:\Python Projects\main\Jego-event-notes\fullybooked\Error Fetching Found"

#     def click_next_page(self):
#         page_str = f"Page {self.page_number}"

#          try:
#             # Click the next page
#             element = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.XPATH, f'//a[@aria-label="{page_str}"]'))
#             )
#             element.click()
#             print(f"Clicked page {self.page_number}")

#             self.page_number += 1

        # except Exception as e:
        #     print(f"Exception while clicking next page: {e}")
        #     return  # Exit the function if unable to click next page

        # # Check for the presence of the error element after clicking next page
        # try:
        #     error_elements = self.driver.find_elements(By.XPATH, NotificationLocators.ERROR_FETCHING)
        #     if error_elements:
        #         # Create folder if it doesn't exist
        #         if not os.path.exists(self.screenshot_folder):
        #             os.makedirs(self.screenshot_folder)
                
        #         # Define the screenshot file path
        #         screenshot_path = os.path.join(self.screenshot_folder, f"Page_{self.page_number - 1}.png")
        #         self.driver.save_screenshot(screenshot_path)
        #         print(f"Error detected on page {self.page_number - 1}, screenshot saved")

        # except Exception as e:
        #     print(f"Exception while checking for error elements: {e}")

