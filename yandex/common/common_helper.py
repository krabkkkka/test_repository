"""
Файл с базовыми методами
"""
from selenium.webdriver.chrome.webdriver import WebDriver


class CommonHelper:
    base_url: str = "https://ya.ru/"
    browser: WebDriver

    def __init__(self, browser: WebDriver, base_url: str | None = None):
        self.base_url = base_url or self.base_url
        self.browser = browser

    def open_url(self):
        self.browser.get(self.base_url)
