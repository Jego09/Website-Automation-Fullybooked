from SupportUtils import *

class Sale():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):
            
            try:

                Sale = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, HeadersLocator.SALE)))
                Sale.click()
                print("-------------Sale Category---------------")
                
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
    books_instance = Sale()
    books_instance.CatTesting()


