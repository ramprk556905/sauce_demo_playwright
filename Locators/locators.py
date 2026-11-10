class Locators:
    '''
    Locators for the website is mentioned in this page
    '''

    '''
    All the Locators for Login Page will be seen below
    '''
    USER_NAME = '//input[@id="user-name"]'
    PASSWORD = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@class="submit-button btn_action"]'
    LOGIN_ERROR = '//h3[@data-test="error"]'


    '''
    All the Locators for Product Listing page is will be seen below
    '''
    PAGE_TITLE = '//span[@class="title"]'
    PRODUCT_NAME = '//div[@class="inventory_item_name "]'
    PRODUCT_PRICE = '//div[@class="inventory_item_price"]'
    ADD_CART_BUTTON = '//button[@class="btn btn_primary btn_small btn_inventory "]'
    SORT_BUTTON = '//span[@class="active_option"]'
    CART_BUTTON = '//a[@class="shopping_cart_link"]'


    '''
    Locators for Product details page is seen below
    '''
    PRODUCT_NAME_DETAILS_PAGE = '//div[@class="inventory_details_name large_size"]'
    BACK_TO_PRODUCTS = '//button[@class="btn btn_secondary back btn_large inventory_details_back_button"]'


    '''
    Locators for the cart page is seen below
    '''
    QTY = '//div[@class="cart_quantity"]'
    CHECKOUT_BUTTON = '//button[@class="btn btn_action btn_medium checkout_button "]'
    CONTINUE_SHOPPING_BUTTON = '//button[@class="btn btn_secondary back btn_medium"]'


    '''
    User Info Locators
    '''
    FIRST_NAME = '//input[@data-test="firstName"]'
    SECOND_NAME = '//input[@data-test="lastName"]'
    ZIP_CODE = '//input[@data-test="postalCode"]'
    CONTINUE_BUTTON = '//button[@data-test="cancel"]'