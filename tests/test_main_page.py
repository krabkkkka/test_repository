import logging

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.common.common_helper import CommonHelper
from yandex.search.search_page_helper import SearchPageHelper
from yandex.search.search_page_process import SearchPageProcess


class TestMainPage:
    @pytest.mark.parametrize(
        "link, search_text",
        [pytest.param("https://tensor.ru/", "тензор", id="search_tensor")],
    )
    def test_main_page(
        self, initialize_browser: WebDriver, link: str, search_text: str
    ):
        logging.info("Открытие страницы поиска")
        common_helper = CommonHelper(browser=initialize_browser)
        common_helper.open_url()

        logging.info("Ввод текста в поле поиска")
        search_page_helper = SearchPageHelper(browser=initialize_browser)
        search_page_helper.fill_search_filed(text=search_text)

        logging.info("Проверка появления подсказки")
        search_page_process = SearchPageProcess()
        initialize_browser.find_element(
            **search_page_process.mini_suggestion
        ).is_displayed()

        logging.info("Поиск через Enter")
        search_page_helper.search()

        logging.info("Проверка первой ссылки")
        search_page_helper.check_first_search_result(link=link)
