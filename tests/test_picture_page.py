from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.common.common_helper import CommonHelper
from yandex.search.search_page_helper import SearchPageHelper


class TestPicturePage:
    def test_picture_page(self, initialize_browser: WebDriver):
        # Открытие страницы поиска
        common_helper = CommonHelper(browser=initialize_browser)
        common_helper.open_url()

        # Клик по полю поиска
        search_page_helper = SearchPageHelper(browser=initialize_browser)
        search_page_helper.open_search_field()

        # Открытие меню сервисов, открытие "Все"

        # Открытие Картинки

        # Проверка перехода на images

        # Открытие первой категории

        # Проверка наличия заголовка в поле поиска

        # Открытие первой картинки

        # Переход на следующую картинку

        # Проверка изменения изображения

        # Возвращение к предыдущей картинке

        # Проверка исходного изображения
