"""
This module contains shared fixtures.
"""
import json

import pytest
import selenium.webdriver

from project_variables import CONFIG_FILE


@pytest.fixture
def config(scope="session"):
    """
    Fixture to read config.json in scope of session
    :param scope:
    :return:
    """

    # Read the file
    with open(CONFIG_FILE) as config_file:
        config_data = json.load(config_file)

    # Assert values are acceptable
    assert config_data["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config_data["implicit_wait"], int)
    assert config_data["implicit_wait"] > 0

    # Return config so it can be used
    return config_data


@pytest.fixture
def browser(config):
    """
    Fixture to initialize webdriver and clean up after test
    """
    # Initialize the WebDriver instance
    if config["browser"] == "Firefox":
        webdriver = selenium.webdriver.Firefox()
    elif config["browser"] == "Chrome":
        webdriver = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        webdriver = selenium.webdriver.Chrome(options=opts)
    else:
        raise ValueError(f"Unknown browser: {config['browser']}")
    # set implicit wait
    webdriver.implicitly_wait(config["implicit_wait"])

    # return the instance
    yield webdriver

    # close the instance
    webdriver.quit()
