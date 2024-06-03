from SupportUtils import *

class Fashion():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):

                Fashion = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_FASHION)))
                Fashion.click()
                print("Clicked Fashion Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = Fashion()
    books_instance.CatTesting()


