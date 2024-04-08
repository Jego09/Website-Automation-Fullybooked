from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from elements import *

class checkout():

    def __init__(self, driver):
        self.driver = driver

    def checkout_complete(self):
        try:
            
            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, HeaderLocators.SEARCH_INPUT))
            )
            search_field.send_keys("9781250326751-2")
            print("Insert a title")
            # Submit the search by pressing ENTER
            search_field.send_keys(Keys.ENTER)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CategoryPageLocators.FIRST_ITEM))
            )

            #clicks the first title within the search perimeter
            p_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CategoryPageLocators.FIRST_ITEM))
            )
            p_elements.click()
            print("Clicked a Title")

            # Check if the add to cart button exists using XPath
            add_cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ItemDescriptionLocators.ADD_TO_CART)))
            # If the add to cart button exists, click on it
            add_cart.click()
            print("Clicked the Add To Cart Button.")

            #Wait for Product added Notification
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, NotificationLocators.NOTIF_ADDED))
            )

            #Opens Cart
            cart_button = self.driver.find_element(By.XPATH, HeaderLocators.CART_BUTTON)
            cart_button.click()
            print("Opens Cart")

            try:
            #Clicks View Cart
                view_cart = self.driver.find_element(By.XPATH, CartHeaderLocators.VIEW_CART)
                view_cart.click()
                print("Clicks View Cart")
            except:
                print("Quantity/Cart not Available")
                self.driver.quit()          

            #Clicks Checkout
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By. XPATH, ShoppingCartLocators.CHECKOUT_CART))
            )
            checkout_button.click()
            print("Clicks Checkout Button")

            text_area = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, ShippingDetailsLocators.NOTES_INPUT))
            )
            text_area.send_keys("Disregard This Order, For testing purposes Only")
            print("Input Disregard Order Text")
            
            ptb_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, ShippingDetailsLocators.PAY_TO_BILLING))
            )
            ptb_button.click()
            print("Clicked Proceed to Billing")

            cod_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PaymentDetailsLocators.COD_BUTTON))
            )
            cod_button.click()
            print("Clicked Cash on Delivery Button")
            tac_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PaymentDetailsLocators.TAC_BUTTON))
            )
            tac_button.click()
            print("Clicked Terms and Condition Button")
            time.sleep(5)

            # checkout button / commented out because it needed to be tested manually.
            # po_button = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, PaymentDetailsLocators.PO_BUTTON)))
            # po_button.click()

        except NoSuchElementException:
            # If the add to cart does not exist, click on the Notify me
            notify_me = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ItemDescriptionLocators.NOTIFY_BUTTON)))
            notify_me.click()
            print("Clicked the Notify Me Button")
        except:
            print("Nothing can be clicked")
            self.driver.quit()

if __name__ == "__main__":
    checkout_instance = checkout()
    checkout_instance.checkout_complete()
