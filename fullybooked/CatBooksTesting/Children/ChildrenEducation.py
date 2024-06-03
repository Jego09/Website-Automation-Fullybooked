from SupportUtils import *

class Education():

    def __init__(self, driver):
        
        self.driver = driver

    def EducationTesting(self):
                
                p_education = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_EDUCATION)))
                p_education.click()
                print("Clicked Education Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()


if __name__ == "__main__":
    books_instance = Education()
    books_instance.EducationTesting()


