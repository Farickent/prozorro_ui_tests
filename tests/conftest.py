import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options




@pytest.fixture(scope="session")
def get_chrome_options():
    options = chrome_options()
    options.add_argument("chrome")  # Open chrome in full window
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1440,900") #size window
    return options


@pytest.fixture(scope="session")
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope="session")
def setup(request, get_webdriver):
    driver = get_webdriver
    url = "https://staging.prozorro.gov.ua/"
    session = request.node
    for item in session.items:
        if item.getparent(pytest.Class) is not None:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", driver)
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def tenders(request, get_webdriver):
    driver = get_webdriver
    url = "https://staging.prozorro.gov.ua/search/tender"
    session = request.node
    for item in session.items:
        if item.getparent(pytest.Class) is not None:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", driver)
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def plans(request, get_webdriver):
    driver = get_webdriver
    url = "https://staging.prozorro.gov.ua/search/plan"
    session = request.node
    for item in session.items:
        if item.getparent(pytest.Class) is not None:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", driver)
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def catalog(request, get_webdriver):
    driver = get_webdriver
    url = "https://staging.prozorro.gov.ua/search/catalog"
    session = request.node
    for item in session.items:
        if item.getparent(pytest.Class) is not None:
            cls = item.getparent(pytest.Class)
            setattr(cls.obj, "driver", driver)
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()












