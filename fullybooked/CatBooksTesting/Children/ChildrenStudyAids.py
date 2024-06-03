from SupportUtils import *

class StudyAids():

    def __init__(self, driver):
        self.driver = driver

    def StudyAidsTesting(self):
                
                Study_Aids = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, CatBooksLocators.H3_STUDY_AIDS)))
                Study_Aids.click()
                print("Clicked Study Aids Category")

                sort_newest = SortBy(self.driver)
                sort_newest.sort_newest()

                page_clicker = PageClicker(self.driver)
                page_clicker.click_next_page()

if __name__ == "__main__":
    books_instance = StudyAids()
    books_instance.StudyAidsTesting()


