from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"chromedriver",)
    browser.maximize_window()
    return browser
