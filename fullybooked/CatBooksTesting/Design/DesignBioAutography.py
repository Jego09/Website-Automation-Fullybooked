from SupportUtils import *

class BioAutography():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):

                BioAutography = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_BIOGRAPHY_AUTOBIOGRAPHY)))
                BioAutography.click()
                print("Clicked Biography & Autobiography Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = BioAutography()
    books_instance.CatTesting()


