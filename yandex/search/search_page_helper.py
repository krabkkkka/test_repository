"""
Файл с основными методами для работы со страницей поиска
"""
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from yandex.common.common_helper import CommonHelper
from yandex.search.search_page import SearchPage


class SearchPageHelper:
    browser: WebDriver

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open_search_field(self) -> None:
        """Клик по полю поиска"""
        CommonHelper(browser=self.browser).wait_until_element_located(**SearchPage().search_field).click()

    def fill_search_filed(self, text: str) -> None:
        """Ввод текста для поиска"""
        CommonHelper(browser=self.browser).wait_until_element_located(
            **SearchPage().search_field
        ).send_keys(text)

    def open_all_services(self) -> None:
        """Открытие всех сервисов"""
        CommonHelper(browser=self.browser).wait_until_element_located(**SearchPage().all_services_button).click()

    def open_picture_service(self) -> None:
        """Открытие раздела Картинки"""
        handles = self.browser.window_handles
        self.browser.find_element(**SearchPage().picture_service_button).click()
        WebDriverWait(driver=self.browser, timeout=5).until(
            expected_conditions.new_window_is_opened(handles)
        )
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def check_first_search_result(self, link: str) -> None:
        """Проверка первого результата поиска"""
        by, value = (
            SearchPage().first_search_result.get("by", By.CSS_SELECTOR),
            SearchPage().first_search_result.get("value").format(link=link),
        )
        CommonHelper(browser=self.browser).wait_until_element_located(by=by, value=value).is_displayed()

    def search(self) -> None:
        """Инициализация поиска через Enter"""
        CommonHelper(browser=self.browser).wait_until_element_located(
            **SearchPage().search_field
        ).send_keys(Keys.ENTER)
