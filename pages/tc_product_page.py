import os
from pages.base import BasePage
from Locators.locators import Locators

class ProductPage(BasePage):
    '''
    The class contains test case for the product page of
    the Sauce Demo website
    '''

    Locators = Locators

    def __init__(self, config,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config.get('filter',{})


    def validate_product_list(self):
        '''
        This function is used to validate that whether all the
        product in the page are listed or not
        '''
        count = self.get_element_count(self.Locators.ADD_CART_BUTTON)
        assert count == 6
        