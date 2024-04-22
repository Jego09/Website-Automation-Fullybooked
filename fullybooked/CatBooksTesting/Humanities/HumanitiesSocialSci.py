from SupportUtils import *

class SocialSci():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):
            try:

                SocialSci = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_SOCIALSCI)))
                SocialSci.click()
                print("Clicked H3_RELIGION Category")

                sort_by = WebDriverWait(self.driver, 10).until(
                     EC.presence_of_element_located((By.XPATH, "//*[@id='category-sort_wrapper']/div"))
                )
                sort_by.click()

                newest = self.driver.find_element(By.XPATH, "//*[@id='oASC newest']")
                newest.click()

                page_number = 1

                while True:
                    
                    page_str = f"Page {page_number}"
                    
                    element = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, f'//a[@aria-label="{page_str}"]')))
                    element.click()
                    print(f"Clicked page {page_number}")
                    
                    page_number += 1
    
            except TimeoutException:
                print("TimeoutException: Error Fetching Occured or Last page reached")
                self.driver.quit()
            
            except NoSuchElementException:
                print("Last page reached")
                self.driver.quit()

if __name__ == "__main__":
    books_instance = SocialSci()
    books_instance.CatTesting()


