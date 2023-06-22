"""
Файл с базовыми методами
"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CommonHelper:
    browser: WebDriver

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open_url(self, url: str) -> None:
        """Открытие url"""
        self.browser.get(url)

    def wait_until_element_located(self, by: str, value: str, timeout: int = 10) -> WebElement:
        """Ожидание видимости элемента"""
        element = WebDriverWait(driver=self.browser, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((by, value))
        )
        return element

    def check_url(self, expected_url: str) -> None:
        """Проверка текущего url"""
        current_url = self.browser.current_url
        assert current_url == expected_url, f"Ожидаемый url: {expected_url}\nПолученный url: {current_url}"
