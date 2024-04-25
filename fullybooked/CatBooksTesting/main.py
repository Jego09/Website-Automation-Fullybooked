from UtilsMain import *
'''
class ChildrenMain(unittest.TestCase):
        
    def setUp(self):
        
        # options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(10)
    
        Books = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
        Books.click()
        print("Clicked Books Category")

        Childrens = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_CHILDRENS)))
        Childrens.click()
        print("Clicked Childrens Category")        

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_b_education(self):
        books_instance = Education(self.driver)
        books_instance.EducationTesting()

    def test_c_juvenile_fiction(self):
        books_instance = JuvenileFiction(self.driver)
        books_instance.CatTesting()
    
    def test_d_juvenile_non_fiction(self):
        books_instance = JuvenileNonFiction(self.driver)
        books_instance.JuvNonTesting()
    
    def test_e_study_aids(self):
        books_instance = StudyAids(self.driver)
        books_instance.StudyAidsTesting()

    def test_f_yafic(self):
        books_instance = YAFic(self.driver)
        books_instance.YAFicTesting()

    def test_g_yafic(self):
        books_instance = YANFic(self.driver)
        books_instance.YANFicTesting()
    
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
    
    def test_m_graphicarts(self):
        books_instance = GraphicArts(self.driver)
        books_instance.CatTesting()
    
    def test_n_househome(self):
        books_instance = HouseHome(self.driver)
        books_instance.CatTesting()

class GraphicNovelMain(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(10)

        Books = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
        actions = ActionChains(self.driver)
        actions.move_to_element(Books).perform()
    
        GN = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_GRAPHIC_NOVEL)))
        GN.click()
        print("Clicked H2_Graphic Novel Category")

    def test_o_gn(self):
        books_instance = GraphicNovel(self.driver)
        books_instance.CatTesting()

    def test_p_manga(self):
        books_instance = Manga(self.driver)
        books_instance.CatTesting()

class HumanitiesMain(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(10)

        Books = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
        actions = ActionChains(self.driver)
        actions.move_to_element(Books).perform()
    
        GN = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CatBooksLocators.H2_HUMANITIES)))
        GN.click()
        print("Clicked H2_HUMANITIES Category")
    
    def test_q_fiction(self):
        books_instance = Fiction(self.driver)
        books_instance.CatTesting()
    
    def test_r_history(self):
        books_instance = History(self.driver)
        books_instance.CatTesting()
    
    def test_s_literary(self):
        books_instance = Literary(self.driver)
        books_instance.CatTesting()

    def test_t_poetry(self):
        books_instance = Poetry(self.driver)
        books_instance.CatTesting

    def test_u_polsci(self):
        books_instance = PolSci(self.driver)
        books_instance.CatTesting()

    def test_v_religion(self):
        books_instance = Religion(self.driver)
        books_instance.CatTesting
    
    def test_w_socialsci(self):
        books_instance = SocialSci(self.driver)
        books_instance.CatTesting()
'''
class HeadersMain(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    # def test_x_bestsellers(self):
    #     books_instance = Bestsellers(self.driver)
    #     books_instance.CatTesting()
    
    def test_y_collections(self):
        books_instance = Collections(self.driver)
        books_instance.CatTesting()
    
    # def test_z_new(self):
    #     books_instance = New(self.driver)
    #     books_instance.CatTesting()
    
    # def test_aa_preorders(self):
    #     books_instance = PreOrders(self.driver)
    #     books_instance.CatTesting()
    
    # def test_ab_sale(self):
    #     books_instance = Sale(self.driver)
    #     books_instance.CatTesting()


# class LifestyleMain(unittest.TestCase):

    # def setUp(self):

    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.fullybookedonline.com")
    #     self.driver.implicitly_wait(10)

    #     Books = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, CatBooksLocators.H1_BOOKS)))
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(Books).perform()

        

if __name__ == "__main__":
    unittest.main()