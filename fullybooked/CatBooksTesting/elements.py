class Login:
    
    #Login Locators in Fullybooked Website
    LOGIN_LOGO = "myAccount"
    USERNAME_TXTBOX = "email"
    PASSWORD_TXTBOX = "password"
    LOGIN_BUTTON = "//*[@id='root']/div/section/header/nav/div[2]/div/div/div/form/div[4]/button"

class HeaderLocators:

    SEARCH_INPUT = "search-field"
    CART_BUTTON = "//*[@id='root']/div/section[1]/header/nav/div[4]/button"
    WISHLIST_BUTTON = "//*[@id='root']/div/section[1]/header/nav/div[3]/a"

class CategoryPageLocators:

    #XPATH Of First & Second Item
    FIRST_ITEM = "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p"
    SECOND_ITEM = "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[2]/a/div[2]/p"
    #Class ID of Items
    PRODUCT_ITEM = "ProductCard-Name"

#***XPATH OF ARIA-LABEL AS PAGE NUMBER
    PAGE_ARIA = "f'//a[@aria-label="
#***XPATH OF PAGE_BUTTON
    PAGE_BUTTON = "//a[@aria-label='Page 1']"
#***Declaring the page number
    PAGE_NUM = 1
#***CONCATENATING STRING AND INT 
    PAGE_STR = f"Page {PAGE_NUM}"
#***FINAL result Combining XPATH_BUTTON, PAGE NUMBER, AND CONCATENATING STR AND INT
    PAGE_LOOP = f'//a[@aria-label="{PAGE_STR}"]'



class ItemDescriptionLocators:

    ADD_TO_CART = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/button"
    NOTIFY_BUTTON = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/section/div/div/button"
    WISHLIST_BUTTON = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[6]/div[1]/button/div"
    
class CartHeaderLocators:

    VIEW_CART = "//*[@id='root']/div/section[1]/header/nav/div[4]/div/div/div[2]/div/a"
    CHECKOUT_BUTTON = "//*[@id='root']/div/section[1]/header/nav/div[4]/div/div/div[2]/div/button"

class ShoppingCartLocators:

    CHECKOUT_CART = "//*[@id='root']/div/div[2]/main/section/div/div[2]/article/article/div[2]/div/ul/div[2]/div/button"

class NotificationLocators:

    #Product was Added to Cart Notification
    NOTIF_CART = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/button"
    NOTIF_WISHLIST = "//*[@id='root']/div/div[1]/div/p"
    ERROR_FETCHING = "//*[@id='root']/div/div[1]/div" 
    ERROR_MESSAGE = "is Triggered"
    NOTIF_GENERAL = "//*[@id='root']/div/div[1]"

class ShippingDetailsLocators:

    NOTES_INPUT = "//*[@id='SHIPPING_STEP']/div[2]/div/div/div/div/div/textarea"
    PAY_TO_BILLING = "//*[@id='SHIPPING_STEP']/div[4]/button"

class PaymentDetailsLocators:
    
    COD_BUTTON = "//*[@id='option-Cash On Delivery']"
    TAC_BUTTON = "//*[@id='termsAndConditions']"
    PO_BUTTON = "//*[@id='BILLING_STEP']/div[4]/button"

class AdminLocators:
    USERNAME = "username"
    PASSWORD = "login"
    SIGN_IN_BUTTON = "//*[@id='login-form']/fieldset/div[3]/div[1]/button/span"

class CatBooksLocators:

    H1_BOOKS = "//*[@id='6']"

#****H2_Under BOOKS 

    H2_CHILDRENS ="//*[@id='9']/figcaption"
    H2_DESIGN = "//*[@id='33']/figcaption"
    H2_GRAPHIC_NOVEL = "//*[@id='72']/figcaption"       
    H2_HUMANITIES = "//*[@id='81']/figcaption"
    H2_LIFESTYLE = "//*[@id='123']/figcaption"
    H2_PROFESSIONAL = "//*[@id='234']/figcaption"

#****H3_UNDER CHILDRENS

    H3_BIBLES = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[1]/a"
    H3_JUVENILE_FICTION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[3]/a"
    H3_JUVENILE_NON_FICTION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[4]/a"
    H3_EDUCATION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[2]/a"
    H3_STUDY_AIDS = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[5]/a"
    H3_YOUNG_ADULT_FICTION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[6]/a"
    H3_YOUNG_ADULT_NON_FICTION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[7]/a"
    
#****H3_UNDER DESIGN

    H3_ARCHITECTURE = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[1]/a"
    H3_ART = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[2]/a"
    H3_FASHION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[3]/a"
    H3_BIOGRAPHY_AUTOBIOGRAPHY = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[4]/a"
    H3_HOUSE_HOME = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[6]/a"
    H3_GRAPHIC_ARTS = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[7]/a"

#****H3_UNDER GRAPHIC NOVELS

    H3_GRAPHIC_NOVEL = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[1]/a"
    H3_MANGA = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[2]/a"

#****H3_UNDER HUMANITIES

    H3_FICTION = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[1]/a"
    H3_HISTORY = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[2]/a"
    H3_LITERARY = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[3]/a"
    H3_POETRY = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[3]/a"
    H3_POLSCI = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[5]/a"
    H3_RELIGION = '//*[@id="root"]/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[6]/a'
    H3_SOCIALSCI = '//*[@id="root"]/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[7]/a'


class CatNonBooksLocators:
    H1_NON_BOOKS = "//*[@id='294']"
#****H2_UNDER NONBOOKS
    H2_ART_SUPPLIES = "//*[@id='root']/div/div[2]/main/section/div/article/div/div[1]/div/div/ul/li[1]/a"
    # H2_CALENDAR_PLANNERS = 
    # H2_CARDS_GIFTWRAP = 
    # H2_CHARACTER = 
    # H2_LIFESTYLE = 
    # H2_NOTEBOOKS_JOURNALS = 
    # H2_SUPPLIES = 