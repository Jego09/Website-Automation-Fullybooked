from SupportUtils import *

class JuvenileNonFiction():

    def __init__(self, driver):
        self.driver = driver

    def JuvNonTesting(self):
                            
                Juvenile_Non_Fiction = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_JUVENILE_NON_FICTION)))
                Juvenile_Non_Fiction.click()
                print("Clicked Juvenile Non Fiction Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = JuvenileNonFiction()
    books_instance.JuvNonTesting()


