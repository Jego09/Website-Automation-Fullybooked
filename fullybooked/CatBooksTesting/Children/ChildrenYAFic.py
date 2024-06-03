from SupportUtils import *

class YAFic():

    def __init__(self, driver):
        self.driver = driver

    def YAFicTesting(self):

                p_yaf = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_YOUNG_ADULT_FICTION)))
                p_yaf.click()
                print("Clicked Young Adult Fiction Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = YAFic()
    books_instance.YAFicTesting()


