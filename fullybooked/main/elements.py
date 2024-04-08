# Search Field XPATH

class Login:
    
    #Locator: ID
    LOGIN_LOGO = "myAccount"
    USERNAME_TXTBOX = "email"
    PASSWORD_TXTBOX = "password"
    USERNAME_INPUT = "btad@fullybookedonline.com"
    PASSWORD_INPUT = "@HOsOCRmzkt4ngZ0YIaKj"
    LOGIN_BUTTON = "//*[@id='root']/div/section/header/nav/div[2]/div/div/div/form/div[4]/button"

class HeaderLocators:

    SEARCH_INPUT = "search-field"
    CART_BUTTON = "//*[@id='root']/div/section[1]/header/nav/div[4]/button"
    WISHLIST_BUTTON = "//*[@id='root']/div/section[1]/header/nav/div[3]/a"

class CategoryPageLocators:

    FIRST_ITEM = "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p"
    SECOND_ITEM = "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[2]/a/div[2]/p"
    PRODUCT_ITEM = "ProductCard-Name"

class ItemDescriptionLocators:

    ADD_TO_CART = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/button"
    NOTIFY_BUTTON = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/section/div/div/button"
    

class CartHeaderLocators:

    VIEW_CART = "//*[@id='root']/div/section[1]/header/nav/div[4]/div/div/div[2]/div/a"
    CHECKOUT_BUTTON = "//*[@id='root']/div/section[1]/header/nav/div[4]/div/div/div[2]/div/button"

class ShoppingCartLocators:

    CHECKOUT_CART = "//*[@id='root']/div/div[2]/main/section/div/div[2]/article/article/div[2]/div/ul/div[2]/div/button"

class NotificationLocators:

    #Product was Added to Cart Notification
    NOTIF_ADDED = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/button"
    ERROR_FETCHING = "//*[@id='root']/div/div[1]/div" 
    ERROR_MESSAGE = "is Triggered"


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
    USERNAME_INPUT = "carllimpiado"
    PASSWORD_INPUT = "3DFE632B5D"
    SIGN_IN_BUTTON = "//*[@id='login-form']/fieldset/div[3]/div[1]/button/span"
