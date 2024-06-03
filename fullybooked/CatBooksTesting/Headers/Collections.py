from SupportUtils import *

class Collections():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):
            
            # try:

                Collections = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, HeadersLocator.COLLECTIONS)))
                self.driver.execute_script("arguments[0].click();", Collections)
                print("-------------Collections Category---------------")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()
                
                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = Collections()
    books_instance.CatTesting()

