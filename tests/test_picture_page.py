import logging

from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.common.common_helper import CommonHelper
from yandex.picture.picture_page_helper import PicturePageHelper, Directions
from yandex.search.search_page_helper import SearchPageHelper


class TestPicturePage:
    def test_picture_page(self, initialize_browser: WebDriver):
        logging.info("Открытие страницы поиска")
        common_helper = CommonHelper(browser=initialize_browser)
        common_helper.open_url(url="https://ya.ru/")

        logging.info("Клик по полю поиска")
        search_page_helper = SearchPageHelper(browser=initialize_browser)
        search_page_helper.open_search_field()

        logging.info("Открытие меню сервисов, открытие \"Все\"")
        open_all_services = SearchPageHelper(browser=initialize_browser)
        open_all_services.open_all_services()

        logging.info("Открытие Картинки")
        open_picture_service = SearchPageHelper(browser=initialize_browser)
        open_picture_service.open_picture_service()

        logging.info("Проверка перехода на images")
        common_helper.check_url(expected_url="https://yandex.ru/images/")

        logging.info("Открытие первой категории")
        picture_page_helper = PicturePageHelper(browser=initialize_browser)
        first_category_name = picture_page_helper.get_first_category_name()
        picture_page_helper.open_first_category()

        logging.info("Проверка наличия заголовка в поле поиска")
        picture_page_helper.check_search_field_value(expected_name=first_category_name)

        logging.info("Открытие первой картинки")
        picture_page_helper.open_first_image()
        expected_src = picture_page_helper.get_image_src()

        logging.info("Переход на следующую картинку")
        picture_page_helper.change_image(direction=Directions.next_direction)

        logging.info("Возвращение к предыдущей картинке")
        picture_page_helper.change_image(direction=Directions.previous_direction)

        logging.info("Проверка исходного изображения")
        picture_page_helper.check_src_image(expected_src=expected_src)
