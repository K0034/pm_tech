"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    """
    Fixture to initialize webdriver and clean up after test
    """

    # initialize the Chromedriver instance
    webdriver = selenium.webdriver.Chrome()

    # set implicit wait
    webdriver.implicitly_wait(5)

    # return the instance
    yield webdriver

    # close the instance
    webdriver.quit()
