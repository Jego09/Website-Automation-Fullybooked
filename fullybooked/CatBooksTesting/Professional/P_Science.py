from SupportUtils import *

class Science():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):

                Science = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_Science)))
                Science.click()
                print("Clicked H3_SCIENCE Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = Science()
    books_instance.CatTesting()