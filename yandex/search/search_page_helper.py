"""
Файл с основными методами для работы со страницей поиска
"""
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.search.search_page_process import SearchPageProcess


class SearchPageHelper:
    browser: WebDriver

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open_search_field(self):
        """Клик по полю поиска"""
        self.browser.find_element(*SearchPageProcess().search_field).click()

    def fill_search_filed(self, text: str) -> None:
        """Ввод текста для поиска"""
        self.browser.find_element(*SearchPageProcess().search_field).send_keys(text)

    def check_first_search_result(self, link: str):
        self.browser.find_element(
            SearchPageProcess().first_search_result[0],
            SearchPageProcess().first_search_result[1].format(link=link)
        ).is_displayed()

    def search(self):
        self.browser.find_element(*SearchPageProcess().search_field).send_keys(Keys.ENTER)
