from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from titleList import generate_random_title
from selenium.common.exceptions import *
from elements import *
import random

class search():
    def __init__(self, driver):
        self.driver = driver
        
    def search_bar(self):
        # for _ in range(5): #repeats the process on a specific value
        print("------------SEARCH_OPEN_PRODUCT PROC--------------")
        try:
            for _ in range (5):
            # Generate a random book title
                random_title = generate_random_title()
                
                # Locate the search field and send the random title via titleList.py
                search_field = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, HeaderLocators.SEARCH_INPUT)))
                search_field.send_keys(random_title)
                # search_field.send_keys("The Count of Monte Cristo")
                print("Inserted a title:", random_title)

                # Enter Key
                search_field.send_keys(Keys.ENTER)
                print("Title Entered")

                # Wait for the first item to load / If no item was detected, EXCEPT condition will be triggered
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, CategoryPageLocators.FIRST_ITEM))
                )
                # try:
                #     WebDriverWait(self.driver, 10).until(
                #         EC.visibility_of_element_located((By.XPATH, NotificationLocators.ERROR_FETCHING))
                #     )
                #     print("Error fetching:", NotificationLocators.ERROR_MESSAGE)
                # except TimeoutError:
                #     print("Category page loaded, but first item not found")
                #     self.driver.quit()
                
                #clicks a random title within the grid
                random_item = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, CategoryPageLocators.PRODUCT_ITEM)))
                elements_p = random.choice(random_item)
                elements_p.click()
                print("Clicked a Random Title")
                
                #waits for Notify Me or Add to cart to be located / Notify me and Add to cart are separated by | 
                # WebDriverWait(self.driver, 15).until(
                #     EC.presence_of_element_located((By.XPATH, ItemDescriptionLocators.ADD_TO_CART)) 
                #     or
                #     EC.presence_of_element_located((By.XPATH, ItemDescriptionLocators.NOTIFY_BUTTON))
                # )
                # print("Product is available")
            
        #if no item was located
        except TimeoutException:
            print("No Items was found or Error Fetching was Triggered")

if __name__ == "__main__":
    search_instance = search()
    search_instance.search_bar()
