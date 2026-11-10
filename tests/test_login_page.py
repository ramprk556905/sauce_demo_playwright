import os
import pytest
from pages.tc_login_page import LoginPage

@pytest.fixture
def login_page(input_data,setup):
    """
    This test will validate the functionality of the login page and verifies that whether user is successfully
    logged in or not
    """
    return LoginPage(input_data, setup)


def test_validate_login_functionality_with_valid_credentials(login_page):
    """
    test to validate the functionality of the login page and verifies that whether user is successfully logged in or not
    """
    login_page.validate_login_functionality_with_valid_credentials(os.getenv('user_name'), os.getenv('password'))

def test_validate_login_functionality_with_invalid_credentials(login_page):
    """
    test to validate the functionality of the login page and verifies that whether user is successfully logged in or not
    """
    login_page.validate_login_functionality_with_invalid_credentials(os.getenv('wrong_username'), os.getenv('wrong_password'))

def test_validate_login_functionality_with_empty_username(login_page):
    """
    test to validate the functionality of the login page and verifies that whether user is successfully logged in or not
    """
    login_page.validate_login_functionality_with_empty_username(os.getenv('empty_user'),os.getenv('password'))    


def test_validate_login_functionality_with_empty_password(login_page):
    """
    test to validate the functionality of the login page and verifies that whether user is successfully logged in or not
    """
    login_page.validate_login_functionality_with_empty_password(os.getenv('user_name'),os.getenv('empty_pwd'))    
