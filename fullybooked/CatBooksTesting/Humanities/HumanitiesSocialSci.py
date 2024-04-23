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

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)

                while True:
                     page_clicker.click_next_page()
    
            except TimeoutException:
                print("TimeoutException: Error Fetching Occured or Last page reached")
                self.driver.quit()
            
            except NoSuchElementException:
                print("Last page reached")
                self.driver.quit()

if __name__ == "__main__":
    books_instance = SocialSci()
    books_instance.CatTesting()


