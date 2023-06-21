from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.common.common_helper import CommonHelper
from yandex.picture.picture_page_helper import PicturePageHelper
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
        open_all_services = SearchPageHelper(browser=initialize_browser)
        open_all_services.open_all_services()

        # Открытие Картинки
        open_picture_service = SearchPageHelper(browser=initialize_browser)
        open_picture_service.open_picture_service()

        # Проверка перехода на images
        common_helper.check_windows_count(expected_windows_count=2)
        initialize_browser.switch_to.window(initialize_browser.window_handles[1])
        common_helper.check_url(expected_url='https://yandex.ru/images/')

        # Открытие первой категории
        picture_page_helper = PicturePageHelper(browser=initialize_browser)
        first_category_name = picture_page_helper.get_first_category_name()
        picture_page_helper.open_first_category()

        # Проверка наличия заголовка в поле поиска
        picture_page_helper.check_search_name(expected_name=first_category_name)

        # Открытие первой картинки
        picture_page_helper.open_first_image()
        expected_src = picture_page_helper.get_scr_first_image()

        # Переход на следующую картинку
        picture_page_helper.next_image()

        # Проверка изменения изображения
        picture_page_helper.check_src_image(expected_src=expected_src)


        # Возвращение к предыдущей картинке
        picture_page_helper.previous_image()

        # Проверка исходного изображения
