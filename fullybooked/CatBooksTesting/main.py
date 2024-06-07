from UtilsMain import *

# class A_ChildrenMain(unittest.TestCase):
        
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

#         Childrens = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_CHILDRENS)))
#         Childrens.click()
#         print("Clicked Childrens Category")        

#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()

#     # def test_b_education(self):
#     #     books_instance = Education(self.driver)
#     #     books_instance.EducationTesting()

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
#         books_instance = YAFic(sef.driver)
#         books_instance.YAFicTesting()

#     def test_g_yafic(self):
#         books_instance = YANFic(self.driver)
#         books_instance.YANFicTesting()
    
# class B_DesignMain(unittest.TestCase):

#     def setUp(self):

#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.fullybookedonline.com")
#         self.driver.implicitly_wait(10)

#         Books = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
#         actions = ActionChains(self.driver)
#         actions.move_to_element(Books).perform()
    
#         Design = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_DESIGN)))
#         Design.click()
#         print("Clicked H2_DESIGN Category")
    
#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()

#     def test_h_architecture(self):
#         books_instance = Architecture(self.driver)
#         books_instance.CatTesting()
    
#     def test_i_art(self):
#         books_instance = Art(self.driver)
#         books_instance.CatTesting()
    
#     def test_j_bioautography(self):
#         books_instance = BioAutography(self.driver)
#         books_instance.CatTesting()
    
#     def test_k_fashion(self):
#         books_instance = Fashion(self.driver)
#         books_instance.CatTesting()
    
#     def test_m_graphicarts(self):
#         books_instance = GraphicArts(self.driver)
#         books_instance.CatTesting()
    
#     def test_n_househome(self):
#         books_instance = HouseHome(self.driver)
#         books_instance.CatTesting()

# class C_GraphicNovelMain(unittest.TestCase):

#     def setUp(self):

#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.fullybookedonline.com")
#         self.driver.implicitly_wait(10)

#         Books = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
#         actions = ActionChains(self.driver)
#         actions.move_to_element(Books).perform()
    
#         GN = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_GRAPHIC_NOVEL)))
#         GN.click()
#         print("Clicked H2_Graphic Novel Category")

#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()
    
#     def test_o_gn(self):
#         books_instance = GraphicNovel(self.driver)
#         books_instance.CatTesting()

#     def test_p_manga(self):
#         books_instance = Manga(self.driver)
#         books_instance.CatTesting()

# class D_HumanitiesMain(unittest.TestCase):

#     def setUp(self):

#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.fullybookedonline.com")
#         self.driver.implicitly_wait(10)

#         Books = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
#         actions = ActionChains(self.driver)
#         actions.move_to_element(Books).perform()
    
#         GN = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_HUMANITIES)))
#         GN.click()
#         print("Clicked H2_HUMANITIES Category")


#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()

#     def test_q_fiction(self):
#         books_instance = Fiction(self.driver)
#         books_instance.CatTesting()
    
#     def test_r_history(self):
#         books_instance = History(self.driver)
#         books_instance.CatTesting()
    
#     def test_s_literary(self):
#         books_instance = Literary(self.driver)
#         books_instance.CatTesting()

#     def test_t_poetry(self):
#         books_instance = Poetry(self.driver)
#         books_instance.CatTesting

#     def test_u_polsci(self):
#         books_instance = PolSci(self.driver)
#         books_instance.CatTesting()

#     def test_v_religion(self):
#         books_instance = Religion(self.driver)
#         books_instance.CatTesting
    
#     def test_w_socialsci(self):
#         books_instance = SocialSci(self.driver)
#         books_instance.CatTesting()

class E_HeadersMain(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def test_a_bestsellers(self):
        books_instance = Bestsellers(self.driver)
        books_instance.CatTesting()
    
    def test_b_collections(self):
        books_instance = Collections(self.driver)
        books_instance.CatTesting()

    def test_c_new(self):
        books_instance = New(self.driver)
        books_instance.CatTesting()
    
    def test_d_preorders(self):
        books_instance = PreOrders(self.driver)
        books_instance.CatTesting()
    
    def test_e_sale(self):
        books_instance = Sale(self.driver)
        books_instance.CatTesting()

# class F_LifestyleMain(unittest.TestCase):

#     def setUp(self):

#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.fullybookedonline.com")
#         self.driver.implicitly_wait(10)

#         Books = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
#         actions = ActionChains(self.driver)
#         actions.move_to_element(Books).perform()
    
#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()
    
#     def test_f_bodymind(self):
#         books_instance = BodyMind(self.driver)
#         books_instance.CatTesting()
    
#     def test_g_games(self):
#         books_instance = Games(self.driver)
#         books_instance.CatTesting()
    
#     def test_h_humor(self):
#         books_instance = Humor(self.driver)
#         books_instance.CatTesting()
    
#     def test_i_sports(self):
#         books_instance = Sports(self.driver)
#         books_instance.CatTesting()
    
#     def test_j_travel(self):
#         books_instance = Travel(self.driver)
#         books_instance.CatTesting()

# class G_ProfessionalMain(unittest.TestCase):

#     def setUp(self):

#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.fullybookedonline.com")
#         self.driver.implicitly_wait(10)
    
#         Books = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
#         actions = ActionChains(self.driver)
#         actions.move_to_element(Books).perform()
    
#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()
    
#     def test_k_businessecon(self):
#         books_instance = BusinessEcon(self.driver)
#         books_instance.CatTesting()
    
#     def test_l_foreignlanguage(self):
#         books_instance = ForeignLanguage(self.driver)
#         books_instance.CatTesting()
    
#     def test_m_languagearts(self):
#         books_instance = LanguageArts(self.driver)
#         books_instance.CatTesting()
    
#     def test_n_psychology(self):
#         books_instance = Psychology(self.driver)
#         books_instance.CatTesting()
    
#     def test_o_science(self):
#         books_instance = Science(self.driver)
#         books_instance.CatTesting()
    
#     def test_p_selfhelp(self):
#         books_instance = SelfHelp(self.driver)
#         books_instance.CatTesting()

#     def test_q_socsci(self):
#         books_instance = SocialSci(self.driver)
#         books_instance.CatTesting()

if __name__ == "__main__":
    unittest.main()