from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    # , executable_path=r"chromedriver",
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    return browser
