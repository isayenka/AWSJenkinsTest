from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage


class MainPage(BasePage):
    url = 'https://www.google.com/'

    @property
    def search_input(self):
        locator = (By.NAME, 'q')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def search_button(self):
        locator = (By.NAME, 'btnK')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def logo_button(self):
        locator = (By.ID, 'logo')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
