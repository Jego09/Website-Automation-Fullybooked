import unittest
from search_open_product import *
from open_pages import *
from login import *
from wishlist_no_acc import *
from checkout_complete import *
from contact_us import *
from store_locator import *
from admin import *

class fullybook(unittest.TestCase):
        
    # not logged in, search, open product, add to cart, checkout (COD or Other Methods) 
    def test_a_search_open_product(self):
        search_instance = search()
        search_instance.search_bar()   
        print("Finished Search, Open Product, Add to Cart, Checkout Testing")
    
    #click blogs, open an article
    def test_b_open_pages(self):
        open_blog = open_pages()
        open_blog.blogs()
        print("Finished Open Pages Testing")

    #logged in, search, open product, add to cart, checkout, (COD or Other Methods)
    def test_c_login(self):
        customer_login = login_customer()
        customer_login.login()
        print("Finished Log In Testing")
    
    #wishlist no account
    def test_d_wishlist(self):
        wishlist_instance = wishlist()
        wishlist_instance.wishlist_no_acc()
        wishlist_instance.wishlist_with_acc()
        print("Finished Wishlist Testing")

    def test_e_checkout_complete(self):    
        checkout_instance = checkout()
        checkout_instance.checkout_complete()
        print("Finished Checkout Testing")

    def test_f_contact_us(self):
        contact_click = contact_us()
        contact_click.click_contact_us()
        print("Finished Contact Us Testing")
    
    def test_g_store_locator(self):
        chat_live = store_locator()
        chat_live.locator()
    
    def test_h_admin_login(self):
        admin_login = admin()
        admin_login.admin_login()

    
if __name__ == "__main__":
    unittest.main()
