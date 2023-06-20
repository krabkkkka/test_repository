import logging

from yandex.common.common_helper import CommonHelper
from yandex.search.search_page_helper import SearchPageHelper
from yandex.search.search_page_process import SearchPageProcess


class TestMainPage:
    def test_main_page(self, initialize_browser):
        link = "https://tensor.ru/"
        search_text = "тензор"

        logging.info("Открытие страницы поиска")
        common_helper = CommonHelper(browser=initialize_browser)
        common_helper.open_url()

        logging.info("Ввод текста в поле поиска")
        search_page_helper = SearchPageHelper(browser=initialize_browser)
        search_page_helper.fill_search_filed(text=search_text)

        logging.info("Проверка появления подсказки")
        search_page_process = SearchPageProcess()
        initialize_browser.find_element(*search_page_process.mini_suggestion).is_displayed()

        logging.info("Поиск через Enter")
        search_page_helper.search()

        logging.info("Проверка первой ссылки")
        search_page_helper.check_first_search_result(link=link)
