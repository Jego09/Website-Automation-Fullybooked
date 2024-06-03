from SupportUtils import *

class YANFic():

    def __init__(self, driver):
        self.driver = driver

    def YANFicTesting(self):
    
                p_yanf = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_YOUNG_ADULT_NON_FICTION)))
                p_yanf.click()
                print("Clicked Young Adult Non Fiction Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = YANFic()
    books_instance.YANFicTesting()


