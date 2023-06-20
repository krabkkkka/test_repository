import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def initialize_browser() -> WebDriver:
    browser = webdriver.Chrome()
    yield browser
    browser.close()
