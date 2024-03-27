from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

class checkout():

    def __init__(self, driver):
        self.driver = driver

    def checkout_complete(self):
        try:

            login_register_button = self.driver.find_element(By.ID, "myAccount")
            login_register_button.click()
            print("Clicked Login/Register Button")
            time.sleep(2)

            username = self.driver.find_element(By.ID, "email")
            username.send_keys("btad@fullybookedonline.com")
            print("Entered Username")

            password = self.driver.find_element(By.ID, "password")
            password.send_keys("@HOsOCRmzkt4ngZ0YIaKj")
            print("Entered Password")

            login_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section/header/nav/div[2]/div/div/div/form/div[4]/button")
            print("Clicked Login Button")
            login_button.click()
            time.sleep(3)

            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search-field")))
            search_field.send_keys("Atomic Habits")
            print("Insert a title")
            # Submit the search by pressing ENTER
            search_field.send_keys(Keys.ENTER)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p")))
            time.sleep(2)

            #clicks a random title within the search perimeter
            p_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p" )))
            p_elements.click()
            print("Clicked a Title")
            time.sleep(4)

            # Check if the add to cart button exists using XPath
            add_cart = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/button")
            # If the add to cart button exists, click on it
            add_cart.click()
            print("Clicked the Add To Cart Button.")
            time.sleep(3)

            #Opens Cart
            cart_button = self.driver.find_element(By.XPATH,"//*[@id='root']/div/section[1]/header/nav/div[4]/button")
            cart_button.click()
            print("Opens Cart")
            time.sleep(3)

            #Clicks View Cart
            view_cart = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section[1]/header/nav/div[4]/div/div/div[2]/div/a")
            view_cart.click()
            print("Clicks View Cart")
            time.sleep(3)

            #Clicks Checkout
            checkout_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/article/article/div[2]/div/ul/div[2]/div/button")
            checkout_button.click()
            print("Clicks Checkout Button")
            time.sleep(3)

            text_area = self.driver.find_element(By.XPATH, "//*[@id='SHIPPING_STEP']/div[2]/div/div/div/div/div/textarea")
            text_area.send_keys("Disregard This Order, For testing purposes Only")
            print("Input Disregard Order Text")
            time.sleep(2)

            ptb_button = self.driver.find_element(By.XPATH, "//*[@id='SHIPPING_STEP']/div[4]/button")
            ptb_button.click()
            time.sleep(1)

            cod_button = self.driver.find_element(By.XPATH, "//*[@id='option-Cash On Delivery']")
            cod_button.click()
            
            tac_button = self.driver.find_element(By.XPATH, "//*[@id='termsAndConditions']")
            tac_button.click()
            time.sleep(2)

            po_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='BILLING_STEP']/div[4]/button")))
            po_button.click()
            time.sleep(4)


        except NoSuchElementException:
            # If the add to cart does not exist, click on the Notify me
            notify_me = self.driver.find_element(By.XPATH,
                '//*[@id="root"]/div/div[2]/main/section[1]/div/article/div[5]/section/div/div/button'
            )
            notify_me.click()
            print("Clicked the Notify Me Button.")
            time.sleep(3)


if __name__ == "__main__":
    checkout_instance = checkout()
    checkout_instance.checkout_complete()
