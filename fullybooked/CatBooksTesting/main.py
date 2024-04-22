from UtilsMain import *

load_dotenv('fullybooked\main\.env')

FB_USERNAME: str = os.getenv('USERNAME_INPUT')
FB_PASSWORD: str = os.getenv('PASSWORD_INPUT')

# class ChildrenMain(unittest.TestCase):
        
#     def setUp(self):
        
#         # options = Options()
#         # options.add_argument('--headless')
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.fullybookedonline.com")
#         self.driver.implicitly_wait(10)
    
#         Books = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
#         Books.click()
#         print("Clicked Books Category")

#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()

#     def test_a_bibles(self):
#         books_instance = Bibles(self.driver)
#         books_instance.BiblesTesting()

#     def test_b_education(self):
#         books_instance = Education(self.driver)
#         books_instance.EducationTesting()

#     def test_c_juvenile_fiction(self):
#         books_instance = JuvenileFiction(self.driver)
#         books_instance.CatTesting()
    
#     def test_d_juvenile_non_fiction(self):
#         books_instance = JuvenileNonFiction(self.driver)
#         books_instance.JuvNonTesting()
    
#     def test_e_study_aids(self):
#         books_instance = StudyAids(self.driver)
#         books_instance.StudyAidsTesting()
    
#     def test_f_yafic(self):
#         books_instance = YAFic(self.driver)
#         books_instance.YAFicTesting()

#     def test_g_yafic(self):
#         books_instance = YANFic(self.driver)
#         books_instance.YANFicTesting()

class DesignMain(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(10)

        Books = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
        actions = ActionChains(self.driver)
        actions.move_to_element(Books).perform()
    
        Design = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_DESIGN)))
        Design.click()
        print("Clicked H2_DESIGN Category")

    def test_h_architecture(self):
        books_instance = Architecture(self.driver)
        books_instance.CatTesting()
    
    def test_i_art(self):
        books_instance = Art(self.driver)
        books_instance.CatTesting()
    
    def test_j_bioautography(self):
        books_instance = BioAutography(self.driver)
        books_instance.CatTesting()
    
    def test_k_fashion(self):
        books_instance = Fashion(self.driver)
        books_instance.CatTesting()
    
    def test_l_gardening(self):
        books_instance = Gardening(self.driver)
        books_instance.CatTesting()
    
    def test_m_graphicarts(self):
        books_instance = GraphicArts(self.driver)
        books_instance.CatTesting()
    
    def test_n_househome(self):
        books_instance = HouseHome(self.driver)
        books_instance.CatTesting()

if __name__ == "__main__":
    unittest.main()