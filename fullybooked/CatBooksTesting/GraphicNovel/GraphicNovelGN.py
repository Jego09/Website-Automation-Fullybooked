from SupportUtils import *

class GraphicNovel():

    def __init__(self, driver):
        self.driver = driver

    def CatTesting(self):

                GraphicNovel = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_GRAPHIC_NOVEL)))
                GraphicNovel.click()
                print("Clicked Graphic Novel Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = GraphicNovel()
    books_instance.CatTesting()


