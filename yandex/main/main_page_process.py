"""
Файл с описанием основных элементов главной страницы
"""
from selenium.webdriver.common.by import By


class MainPageProcess:
    search_field = (By.CSS_SELECTOR, "selector")
    search_suggestion = (By.CSS_SELECTOR, "selector")
