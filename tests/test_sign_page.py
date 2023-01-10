"""
File contains test scenarios for sign page
"""
import pytest

from pages.sign_page import SignPage
from pytest_markers import link_to_test


@pytest.mark.smoke
@link_to_test("http://my_test_management_tool.pl")
def test_sign_page_content(browser):
    """
    Test check page content of sign page
    """
    sign_page = SignPage(browser)
    # Given Sign Page opened
    sign_page.open_page()
    sign_page.accept_cookies()
    # Then header has value "Sign In"
    assert "Sign In" == sign_page.get_header_text()
    # And Title has value "Sign In to Paramount+ International (INTL)"
    assert "Sign In to Paramount+ International (INTL)" == sign_page.get_page_title()
    # And sign in form exists
    assert sign_page.email_input.is_displayed()
    assert sign_page.password_input.is_displayed()
    assert sign_page.continue_button.is_displayed()
    assert sign_page.continue_button.get_property("disabled") is False


def test_sign_wrong_credentials(browser):
    """
    Test check handling sign with wrong credentials
    """
    sign_page = SignPage(browser)
    # Given Sign Page opened
    sign_page.open_page()
    sign_page.accept_cookies()
    # When sign in with wrong credentials
    sign_page.fill_sign_in_form(email="ala@ma.kota", password="test")
    # Then error message appears
    assert sign_page.error_message.is_displayed()
    # And error message is equal to "Invalid email and/or password"
    assert "Invalid email and/or password" == sign_page.error_message.text
