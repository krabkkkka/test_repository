"""
Файл с описанием основных элементов главной страницы
"""
from selenium.webdriver.common.by import By


class MainPageProcess:
    search_field = dict(by=By.CSS_SELECTOR, value="selector")
    search_suggestion = dict(by=By.CSS_SELECTOR, value="selector")
