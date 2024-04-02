from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from titleList import generate_random_title, store_title
from get_book_titles import get_titles_from_file
from selenium.common.exceptions import NoSuchElementException
import random

class search():
    def __init__(self, driver):
        self.driver = driver
        
    def search_bar(self):
        # for _ in range(5): #repeats the process on a specific value
        try:
            for _ in range (5):
            # Generate a random book title
                random_title = generate_random_title()
                
                # Locate the search field and send the random title
                search_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "search-field")))
                search_field.send_keys(random_title)
                print("Insert a title")
                # Submit the search by pressing ENTER
                search_field.send_keys(Keys.ENTER)
                print("Entered a Title")
                
                # Wait for the first item to load
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p")))
                time.sleep(2)
                
                #clicks a random title within the search perimeter
                p_elements = WebDriverWait(self.driver, 10).until(
                    (EC.presence_of_all_elements_located((By.CLASS_NAME, "ProductCard-Name"))))
                elements_p = random.choice(p_elements)
                elements_p.click()
                print("Clicked a Random Title")
                time.sleep(10)

        except NoSuchElementException:
                # If the add to cart does not exist, click on the Notify me
                notify_me = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/section/div/div/button")
                notify_me.click()
                print("Clicked the Notify Me Button.")
                time.sleep(3)
                    

if __name__ == "__main__":
    search_instance = search()
    search_instance.search_bar()
