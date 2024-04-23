from SupportUtils import *

class YANFic():

    def __init__(self, driver):
        self.driver = driver

    def YANFicTesting(self):
            try:

                p_yanf = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_YOUNG_ADULT_NON_FICTION)))
                p_yanf.click()
                print("Clicked Young Adult Non Fiction Category")

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
    books_instance = YANFic()
    books_instance.YANFicTesting()


