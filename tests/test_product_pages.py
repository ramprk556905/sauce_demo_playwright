import pytest
from pages.tc_product_page import ProductPage
from pages.tc_login_page import LoginPage


@pytest.fixture
def login_into_product_page(input_data,setup):
    '''
    This function is used to login into the sauce demo page
    '''
    product_page = ProductPage(input_data,setup)
    LoginPage.login(product_page)
    return product_page

def test_validate_product_list(login_into_product_page):
    '''
    This function is used to validate that whether all the
    product in the page are listed or not
    '''
    login_into_product_page.validate_product_list()
