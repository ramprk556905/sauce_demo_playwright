import os
from pages.base import BasePage
from Locators.locators import Locators

class LoginPage(BasePage):
    '''
    The test cases for the Login pages is present here
    '''

    Locators = Locators

    def __init__(self, config, *args, **kwargs):
        '''
        Getting input data from .yml file
        '''
        super().__init__(*args,**kwargs)
        self.config = config.get('login',{})

    def validate_login_functionality_with_valid_credentials(self,username,password):
        '''
        This function is used to validate the login functionality of the login
        with the valid credentials
        '''
        self.fill_input_text(self.Locators.USER_NAME,username)
        self.fill_input_text(self.Locators.PASSWORD,password)
        self.click_element(self.Locators.LOGIN_BUTTON)
        assert self.get_element_text(self.Locators.PAGE_TITLE) == 'Products'


    def validate_login_functionality_with_invalid_credentials(self,username,password):
        '''
        This function is used to validate the login functionality of the login 
        with the invalid credentials
        '''
        self.fill_input_text(self.Locators.USER_NAME,username)
        self.fill_input_text(self.Locators.PASSWORD,password)
        self.click_element(self.Locators.LOGIN_BUTTON)
        assert self.get_element_text(self.Locators.LOGIN_ERROR) == 'Epic sadface: Username and password do not match any user in this service'

    def validate_login_functionality_with_empty_username(self,username,password):
        '''
        This function is used to validate the login functionality of the login 
        with the empty user name
        '''
        self.fill_input_text(self.Locators.USER_NAME,username)
        self.fill_input_text(self.Locators.PASSWORD,password)
        self.click_element(self.Locators.LOGIN_BUTTON)
        assert self.get_element_text(self.Locators.LOGIN_ERROR) == 'Epic sadface: Username is required'

    def validate_login_functionality_with_empty_password(self,username,password):
        '''
        This function is used to validate the login functionality of the login 
        with the empty password
        '''
        self.fill_input_text(self.Locators.USER_NAME,username)
        self.fill_input_text(self.Locators.PASSWORD,password)
        self.click_element(self.Locators.LOGIN_BUTTON)
        assert self.get_element_text(self.Locators.LOGIN_ERROR) == 'Epic sadface: Password is required'


    @classmethod
    def login(cls,page:BasePage):
        '''
        This function is used to validate the login functionality of the login
        with the valid credentials
        '''
        page.fill_input_text(cls.Locators.USER_NAME,os.getenv('user_name'))
        page.fill_input_text(cls.Locators.PASSWORD,os.getenv('password'))
        page.click_element(cls.Locators.LOGIN_BUTTON)
        assert page.get_element_text(cls.Locators.PAGE_TITLE) == 'Products'