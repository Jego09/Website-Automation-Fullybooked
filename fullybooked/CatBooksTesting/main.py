from UtilsMain import *

load_dotenv('fullybooked\main\.env')

FB_USERNAME: str = os.getenv('USERNAME_INPUT')
FB_PASSWORD: str = os.getenv('PASSWORD_INPUT')

class headerBooks(unittest.TestCase):
        
    def setUp(self):
        
        # options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        print("Open Chrome")
        self.driver.implicitly_wait(10)
    
        Books = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
        Books.click()
        print("Clicked Books Category")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_a_bibles(self):
        books_instance = Bibles(self.driver)
        books_instance.BiblesTesting()

    def test_b_education(self):
        books_instance = Education(self.driver)
        books_instance.EducationTesting()

    def test_c_juvenile_fiction(self):
        books_instance = JuvenileFiction(self.driver)
        books_instance.CatTesting()
    
    def test_d_juvenile_non_fiction(self):
        books_instance = JuvenileNonFiction(self.driver)
        books_instance.JuvNonTesting()
    
    # def test_e_study_aids(self):
    #     books_instance = StudyAids(self.driver)
    #     books_instance.StudyAidsTesting()
    
    # def test_f_yafic(self):
    #     books_instance = YAFic(self.driver)
    #     books_instance.YAFicTesting()

    # def test_g_yafic(self):
    #     books_instance = YANFic(self.driver)
    #     books_instance.YANFicTesting()
    
if __name__ == "__main__":
    unittest.main()