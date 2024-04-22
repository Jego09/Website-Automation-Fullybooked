from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from titleList import generate_random_title
import random
from elements import *
from selenium.common.exceptions import TimeoutException

class wishlist():
    try:
        def __init__(self, driver):
            self.driver = driver

        def wishlist_with_acc(self):
            
            print("------------WISHLIST PROC--------------")

            random_title = generate_random_title()
            
            # Locate the search field and send the random title
            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, HeaderLocators.SEARCH_INPUT)))
            search_field.send_keys(random_title)
            print("Insert a title")
            
            # Submit the search by pressing ENTER
            search_field.send_keys(Keys.ENTER)
            print("Entered a Title")

            # Wait for the first item to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CategoryPageLocators.FIRST_ITEM)))
            
            #clicks a random title within the search perimeter
            p_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, CategoryPageLocators.PRODUCT_ITEM)))
            elements_p = random.choice(p_elements)
            elements_p.click()
            print("Clicked a Random Title")

            add_wishlist = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ItemDescriptionLocators.WISHLIST_BUTTON))
            )
            add_wishlist.click()
            print("Added to Wishlist")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, NotificationLocators.NOTIF_WISHLIST))
            )

            click_wishlist = self.driver.find_element(By.XPATH, HeaderLocators.WISHLIST_BUTTON)
            click_wishlist.click()
            time.sleep(3)
            print("End of Wishlist")
    
    except TimeoutException:
        print("No item was selected within the given timeframe.")

if __name__ == "__main__":    
    wishlist_instance = wishlist()
    wishlist_instance.wishlist_with_acc()

