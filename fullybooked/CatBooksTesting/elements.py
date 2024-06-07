class NotificationLocators:

    #Product was Added to Cart Notification
    NOTIF_CART = "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[5]/button"
    NOTIF_WISHLIST = "//*[@id='root']/div/div[1]/div/p"
    # ERROR_FETCHING = "//*[@id='root']/div/div[1]/div" 
    ERROR_FETCHING = '//*[@id="root"]/div/div[1]/div'
    # ERROR_FETCHING = "//body/div[@id='root']/div[1]/div[1]/div[1]/p[1]"
    # ERROR_FETCHING = "Notification Notification_type_error Notification_is_opening" 
    ERROR_MESSAGE = "is Triggered"
    NOTIF_GENERAL = "//*[@id='root']/div/div[1]" 
    
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

#****H3_UNDER LIFESTYLE

    H3_Body_Mind = "//figcaption[contains(text(),'Body & Mind & Spirit')]"
    H3_Cooking = "//figcaption[contains(text(),'Cooking')]"
    H3_Family = "//figcaption[contains(text(),'Family')]"
    H3_Games = "//header/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/a[7]/figcaption[1]"
    H3_Health = "//figcaption[contains(text(),'Health & Fitness')]"
    H3_Humor = "//figcaption[contains(text(),'Humor')]"
    H3_Sports = "//figcaption[contains(text(),'Sports & Recreation')]"
    H3_Travel = "//figcaption[contains(text(),'Travel')]"    

#****H3_UNDER PROFESSIONAL

    H3_BusinessEcon = "//figcaption[contains(text(),'Business & Economics')]"
    H3_ForeignLanguage = "//figcaption[contains(text(),'Foreign Language Study')]"
    H3_LanguageArts = "//figcaption[contains(text(),'Language Arts & Disciplines')]"
    H3_Psychology = "//figcaption[contains(text(),'Psychology')]"
    H3_Science = "//figcaption[contains(text(),'Science')]"
    H3_SocSci = "//header/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/a[17]/figcaption[1]"
    H3_SelfHelp = "//header/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/a[16]/figcaption[1]"

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

class SortByLocators:

    NEWEST = "//*[@id='oASC newest']"
    LOW_TO_HIGH = '//*[@id="oASC price"]'
    HIGH_TO_LOW = '//*[@id="oDESC price"]'
    BESTSELLING = '//*[@id="oASC bestseller_rank"]'

class HeadersLocator:

    BESTSELLERS = '//*[@id="495"]/figcaption'
    COLLECTIONS = '//*[@id="2332"]/figcaption'
    NEW = '//*[@id="498"]'
    PREORDERS = '//*[@id="501"]'
    SALE = '//*[@id="504"]'
    