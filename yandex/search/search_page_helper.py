"""
Файл с основными методами для работы со страницей поиска
"""
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from yandex.common.common_helper import CommonHelper
from yandex.search.search_page_process import SearchPageProcess


class SearchPageHelper:
    browser: WebDriver

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open_search_field(self):
        """Клик по полю поиска"""
        self.browser.find_element(**SearchPageProcess().search_field).click()

    def fill_search_filed(self, text: str) -> None:
        """Ввод текста для поиска"""
        self.browser.find_element(**SearchPageProcess().search_field).send_keys(text)

    def open_all_services(self):
        """Открытие всех сервисов"""
        self.browser.find_element(**SearchPageProcess().all_services_button).click()

    def open_picture_service(self):
        """Открытие раздела Картинки"""
        self.browser.find_element(**SearchPageProcess().picture_service_button).click()

    def check_first_search_result(self, link: str):
        by, value = (
            SearchPageProcess().first_search_result.get("by", By.CSS_SELECTOR),
            SearchPageProcess().first_search_result.get("value").format(link=link),
        )
        CommonHelper(browser=self.browser).wait_until_element_located(by=by, value=value)
        self.browser.find_element(by=by, value=value).is_displayed()

    def search(self):
        self.browser.find_element(**SearchPageProcess().search_field).send_keys(Keys.ENTER)
