import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options




@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument("chrome")  # Open chrome in full window
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1440,900") #size window
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://staging.prozorro.gov.ua/"
    if request.cls is not None:
       request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def tenders(request, get_webdriver, ):
    driver = get_webdriver
    url = "https://staging.prozorro.gov.ua/search/tender"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()











