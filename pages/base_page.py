"""
BasePage class
"""
from retry import retry
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """
    Base class for all pages
    """

    def __init__(self, browser: WebDriver):
        self.driver = browser
        self.base_locators = BasePageLocators()

    @property
    def accept_all_button(self) -> WebElement:
        """
        Return accept all button from cookies popup
        :return:
        """
        return self.driver.find_element(*self.base_locators.accept_all_button)

    @retry(tries=3, delay=2)
    def accept_cookies(self):
        """
        Accept all cookies
        :return:
        """
        self.accept_all_button.click()


class BasePageLocators:
    """
    Base page locators
    """

    def __init__(self):
        self.accept_all_button = (By.ID, "onetrust-accept-btn-handler")
