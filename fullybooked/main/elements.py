# Search Field XPATH

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

class ShippingDetailsLocators:

    NOTES_INPUT = "//*[@id='SHIPPING_STEP']/div[2]/div/div/div/div/div/textarea"
    PAY_TO_BILLING = "//*[@id='SHIPPING_STEP']/div[4]/button"

class PaymentDetailsLocators:
    
    COD_BUTTON = "//*[@id='option-Cash On Delivery']"
    TAC_BUTTON = "//*[@id='termsAndConditions']"
    PO_BUTTON = "//*[@id='BILLING_STEP']/div[4]/button"