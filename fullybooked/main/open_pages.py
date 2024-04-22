from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import random

class open_pages():

    def __init__(self, driver):
        self.driver = driver

    def blogs(self):
        #for _ in range(2):
            print("------------OPEN_PAGES(BLOGS) PROC--------------")
            blog_button = self.driver.find_element(By.XPATH, "//*[@id='2459']/figcaption")
            blog_button.click()
            print("Clicked the blog button")
            time.sleep(2)

            h3_elements = WebDriverWait(self.driver, 10).until(
                (EC.presence_of_all_elements_located((By.CLASS_NAME, "BlogList-ListItemTitle"))))
            random_h3 = random.choice(h3_elements)
            random_h3.click()
            print("Opens an article")
            time.sleep(5)

if __name__ == "__main__":
    open_blog = open_pages()
    open_blog.blogs()
