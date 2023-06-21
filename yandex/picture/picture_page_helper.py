"""
Файл с основными методами для работы со страницей "Картинки"
"""
from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.common.common_helper import CommonHelper
from yandex.picture.picture_page_process import PicturePageProcess


class PicturePageHelper:
    browser: WebDriver

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def get_first_category_name(self) -> str:
        category = CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().first_category)
        return category.get_attribute('data-grid-text')

    def open_first_category(self):
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().first_category).click()

    def check_search_name(self, expected_name):
        search_name = CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().search_field)
        assert search_name.get_attribute('value') == expected_name, 'error text'

    def open_first_image(self):
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().first_image).click()


        # TODO: проверить что открылось изображение (wait_until_element_located + is_displayed + retry)

    # TODO: Добавить метод для получения из открытого изображения attribute = src
    def get_scr_first_image(self):
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().src_first_image).get_attribute('src')

    # TODO: Добавить метод для перехода на следующее изображение (по идее можно прокинуть исходный срц + дождаться изменения срц => картинка сменилась)
    def next_image(self):
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().next_image).click()

    def get_src_next_image(self):
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().src_first_image).get_attribute('src')

    # TODO: Добавить метод для перехода на прошлое изображение
    def previous_image(self):
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().previous_image).click()

    # TODO: Добавить метод для проверки ожидаемого src c полученным (получение текущего можно использовать из туду выше)
    def check_src_image(self, expected_src):
        src = CommonHelper(browser=self.browser).wait_until_element_located(**PicturePageProcess().src_first_image)
        assert src.get_attribute('value') == expected_src, 'error text'

    # По тесту будет что-то типа: открыли изображение - получили срц - перешли на новое изображение -
    # через retry дождались смены срц - перейти на прошлое изображение - через retry дождаться смены срц на начальное
