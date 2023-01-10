"""
File contains SignPage class
"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage, BasePageLocators


class SignPage(BasePage):
    """
    Page object class for SignPage
    """

    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.driver = browser
        self.url = "https://www.paramountplus.com/intl/signin/"
        self._locators = SignPageLocators()

    @property
    def error_message(self) -> WebElement:
        """
        Get error message
        :return: WebElement
        """
        return self.driver.find_element(*self._locators.error_message)

    @property
    def email_input(self) -> WebElement:
        """
        Returns email input
        :return: WebElement
        """
        return self.driver.find_element(*self._locators.email_input)

    @property
    def header(self) -> WebElement:
        """
        Returns header
        :return: WebElement
        """
        return self.driver.find_element(*self._locators.header)

    @property
    def password_input(self) -> WebElement:
        """
        Returns password input
        :return: WebElement
        """
        return self.driver.find_element(*self._locators.password_input)

    @property
    def continue_button(self) -> WebElement:
        """
        Returns continue button
        :return: WebElement"""
        return self.driver.find_element(*self._locators.continue_button)

    @property
    def forgot_password_link(self) -> WebElement:
        """
        Returns forgot password link
        :return: WebElement"""
        return self.driver.find_element(*self._locators.forgot_password_link)

    def fill_sign_in_form(self, email: str, password: str, submit: bool = True) -> None:
        """
        Fills sign in form
        :param email: str
        :param password: str
        :param submit: bool if yes form will be also submitted
        """
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        if submit:
            self.continue_button.click()

    def go_to_forgot_password_page(self) -> None:
        """
        Goes to forgot password page
        """
        self.forgot_password_link.click()

    def get_header_text(self) -> str:
        """
        Returns header text
        :return: str
        """
        return self.header.text

    def get_page_title(self) -> str:
        """
        Returns page title
        :return: str
        """
        return self.driver.title

    def open_page(self) -> None:
        """
        Go to sign page
        :return:
        """
        self.driver.get(self.url)


class SignPageLocators(BasePageLocators):
    """
    Class to holds all locators for SignPage
    """

    def __init__(self):
        super().__init__()
        self.error_message = (By.CSS_SELECTOR, "#error-message")
        self.header = (By.CSS_SELECTOR, ".steps-header")
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.continue_button = (By.CSS_SELECTOR, ".button")
        self.forgot_password_link = (By.LINK_TEXT, "Forgot")
