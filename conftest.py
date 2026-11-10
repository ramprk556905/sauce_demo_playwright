import os
import dotenv
import yaml
import pytest
from playwright.sync_api import Playwright
from datetime import datetime

INPUT_DATA = '--input-data'
INPUT_DATA_TEST_DATA_KEY = 'test_data'
dotenv.load_dotenv()

def pytest_addoption(parser):
    parser.addoption(INPUT_DATA,
                     action = 'store',
                     default=rf"{os.getcwd()}\input_test_data.yml",
                     help='Specify the location of the YAML file from which to read input data')


@pytest.fixture(scope='function')
def setup(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True, args=['--start-maximized'])
    page = browser.new_page(no_viewport=True)
    page.set_default_timeout(50000)
    page.goto(os.getenv('base_url'))
    yield page
    browser.close()

@pytest.fixture(scope='session')
def input_data(pytestconfig):
    '''
    Return the dictionary of input data retrieved from an external YAML source
    '''
    data = {}
    input_data_file_location = str(pytestconfig.getoption(INPUT_DATA))
    if input_data_file_location and os.path.exists(input_data_file_location):
        with open(input_data_file_location) as data_file:
            data = yaml.safe_load(data_file).get(INPUT_DATA_TEST_DATA_KEY,{})

    return data