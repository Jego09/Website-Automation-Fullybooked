from SupportUtils import *

class PreOrders():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):

                PreOrders = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, HeadersLocator.PREORDERS)))
                PreOrders.click()
                print("-------------PreOrders Category---------------")
                
                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = PreOrders()
    books_instance.CatTesting()


