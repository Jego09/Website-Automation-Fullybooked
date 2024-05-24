from utils import *

load_dotenv('fullybooked\main\.env')

FB_USERNAME: str = os.getenv('USERNAME_INPUT')
FB_PASSWORD: str = os.getenv('PASSWORD_INPUT')

# class AdminTest(unittest.TestCase):    

#     def test_admin_login(self):
#         admin_instance = admin()
#         admin_instance.admin_login()

class FullyBookTest(unittest.TestCase):
        
    def setUp(self):
        
        # options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.fullybookedonline.com")
        self.driver.implicitly_wait(10)

        # login_register_button = self.driver.find_element(By.ID, Login.LOGIN_LOGO) 
        # login_register_button.click()
        # # print("Clicked Login/Register Button")

        # username = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, Login.USERNAME_TXTBOX)))
        # username.send_keys(FB_USERNAME)
        # # print("Entered Username")

        # password = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, Login.PASSWORD_TXTBOX)))
        # password.send_keys(FB_PASSWORD)
        # # print("Entered Password")

        # login_button = self.driver.find_element(By.XPATH, Login.LOGIN_BUTTON)
        # # print("Clicked Login Button")
        # login_button.click()
        # time.sleep(2)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_a_search_open_product(self):
        search_instance = search(self.driver)
        search_instance.search_bar()   
        print("Finished Search, Open Product")

    def test_b_open_pages(self):
        open_blog = open_pages(self.driver)
        open_blog.blogs()
        print("Finished Open Pages Testing")

    def test_c_wishlist(self):
        wishlist_instance = wishlist(self.driver)
        wishlist_instance.wishlist_with_acc()
        print("Finished Wishlist Testing")

    def test_d_checkout_complete(self):    
        checkout_instance = checkout(self.driver)
        checkout_instance.checkout_complete()
        print("Finished Checkout Testing")

    def test_e_contact_us(self):
        contact_click = contact_us(self.driver)
        contact_click.click_contact_us()
        print("Finished Contact Us Testing")

    def test_f_store_locator(self):
        chat_live = store_locator(self.driver)
        chat_live.locator()

    # def test_g_cancel_order(self):

if __name__ == "__main__":
    unittest.main()