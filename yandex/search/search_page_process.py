"""
Файл с описанием основных элементов страницы поиска
"""
from selenium.webdriver.common.by import By


class SearchPageProcess:
    search_field = (By.CSS_SELECTOR, "input[class*=\"search3__input\"]")
    all_services_button = (By.CSS_SELECTOR, "a[title=\"Все сервисы\"]")
    mini_suggestion = (By.CLASS_NAME, "mini-suggest__popup-content")
    first_search_result = (By.CSS_SELECTOR, "li[data-cid=\"0\"] a[href=\"{link}\"]:last-child")
