"""
Файл с базовыми методами
"""
from retrying import retry
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CommonHelper:
    base_url: str = "https://ya.ru/"
    browser: WebDriver

    def __init__(self, browser: WebDriver, base_url: str | None = None):
        self.base_url = base_url or self.base_url
        self.browser = browser

    def open_url(self, url: str | None = None):
        self.browser.get(url or self.base_url)

    def wait_until_element_located(self, by: str, value: str, timeout: int = 10):
        element = WebDriverWait(driver=self.browser, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((by, value))
        )
        return element

    def check_url(self, expected_url: str):
        current_url = self.browser.current_url
        assert current_url == expected_url, f"Ожидаемый url: {expected_url}\nПолученный url: {current_url}"

    @retry(stop_max_attempt_number=5, wait_fixed=1000)
    def check_windows_count(self, expected_windows_count: int):
        assert len(self.browser.window_handles) == expected_windows_count, "error text"

# EXAMPLE:
# common_helper = CommonHelper(base_url="https://yandex.ru/images/", browser=self.browser)
# common_helper.check_url(expected_url=common_helper.base_url)
