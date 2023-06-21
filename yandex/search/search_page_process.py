"""
Файл с описанием основных элементов страницы поиска
"""
from selenium.webdriver.common.by import By


class SearchPageProcess:
    search_field = dict(by=By.CSS_SELECTOR, value='input[class*="search3__input"]')
    mini_suggestion = dict(by=By.CLASS_NAME, value="mini-suggest__popup-content")
    first_search_result = dict(by=By.CSS_SELECTOR, value='li[data-cid="0"] a[href="{link}"]:last-child')
    all_services_button = dict(by=By.CSS_SELECTOR, value='a[title="Все сервисы"]')
    picture_service_button = dict(by=By.CSS_SELECTOR, value='a[aria-label="Картинки"]')
    # Картинки
    # TODO: Картинки открываются в новой вкладке, нужно будет свичнуться на новое окно
