"""
Файл с основными методами для работы со страницей "Картинки"
"""
from retrying import retry
from selenium.webdriver.chrome.webdriver import WebDriver

from yandex.common.common_helper import CommonHelper
from yandex.picture.picture_page import PicturePage


class Directions:
    next_direction = "next"
    previous_direction = "previous"


class PicturePageHelper:
    browser: WebDriver

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def get_first_category_name(self) -> str:
        """Получение текста первой категории"""
        category = CommonHelper(browser=self.browser).wait_until_element_located(**PicturePage().first_category)
        return category.get_attribute("data-grid-text")

    def open_first_category(self) -> None:
        """Открытие первой категории"""
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePage().first_category).click()

    def check_search_field_value(self, expected_name: str) -> None:
        """Проверка текста в поле поиска"""
        actual_search_name = (
            CommonHelper(browser=self.browser)
            .wait_until_element_located(**PicturePage().search_field)
            .get_attribute("value")
        )
        assert (
            actual_search_name == expected_name
        ), f"Ожидаемое значение в поле поиска: {expected_name}\nПолученное значение:{actual_search_name}"

    def open_first_image(self) -> None:
        """Открытие первого изображения"""
        CommonHelper(browser=self.browser).wait_until_element_located(**PicturePage().first_image).click()
        self.browser.find_element(**PicturePage().opened_image)

    def get_image_src(self) -> str:
        """Получение src текущего изображения"""
        return self.browser.find_element(**PicturePage().opened_image).get_attribute("src")

    @retry(stop_max_attempt_number=5, wait_fixed=1000)
    def wait_until_image_changed(self, old_image_src: str) -> None:
        """Ожидание смены изображения"""
        new_image_src = self.get_image_src()
        assert new_image_src != old_image_src, "Изображение не изменилось"

    def change_image(self, direction: str = Directions.next_direction) -> str:
        """Переключение изображение (следующее / предыдущее)"""
        direction_map = dict(
            next=PicturePage().next_image,
            previous=PicturePage().previous_image,
        )
        assert direction in direction_map.keys()

        image_object = direction_map[direction]
        current_src = self.get_image_src()
        self.browser.find_element(**image_object).click()
        self.wait_until_image_changed(old_image_src=current_src)
        self.browser.find_element(**PicturePage().opened_image)
        return self.get_image_src()

    def check_src_image(self, expected_src: str) -> None:
        """Проверка src текущего изображения"""
        self.browser.find_element(**PicturePage().opened_image)
        current_src = self.get_image_src()
        assert current_src == expected_src, "Полученное изображение отличается от ожидаемого"
