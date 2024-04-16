from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from get_book_titles import get_titles_from_file
from titleList import generate_random_title
import random

class login_customer():
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        try:
            
            login_register_button = self.driver.find_element(By.ID, "myAccount")
            login_register_button.click()
            print("Clicked Login/Register Button")
            time.sleep(5)

            username = self.driver.find_element(By.ID, "email")
            username.send_keys("btad@fullybookedonline.com")
            print("Entered Username")

            password = self.driver.find_element(By.ID, "password")
            password.send_keys("@HOsOCRmzkt4ngZ0YIaKj")
            print("Entered Password")

            login_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section/header/nav/div[2]/div/div/div/form/div[4]/button")
            print("Clicked Login Button")
            login_button.click()
            time.sleep(2)

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

            # Check if the first button exists using XPath
            add_cart = self.driver.find_element(By.XPATH,
                '//*[@id="root"]/div/div[2]/main/section[1]/div/article/div[5]/button'
            )
            add_cart.click()
            print("Clicked the Add To Cart Button.")
            time.sleep(3)

            cart_button = self.driver.find_element(By.XPATH,"//*[@id='root']/div/section[1]/header/nav/div[4]/button")
            cart_button.click()
            time.sleep(3)

            view_cart = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section[1]/header/nav/div[4]/div/div/div[2]/div/a")
            view_cart.click()
            time.sleep(3)

            checkout_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/article/article/div[2]/div/ul/div[2]/div/button")
            checkout_button.click()
            time.sleep(3)

        except NoSuchElementException:
            # If the add to cart does not exist, click on the Notify me
            notify_me = self.driver.find_element(By.XPATH,
                '//*[@id="root"]/div/div[2]/main/section[1]/div/article/div[5]/section/div/div/button'
            )
            notify_me.click()
            print("Clicked the Notify Me Button.")
            time.sleep(3)
          
if __name__ == "__main__":
    customer_login = login_customer()
    customer_login.login()


