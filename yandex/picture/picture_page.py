"""
Файл с описанием основных элементов страницы "Картинки"
"""
from selenium.webdriver.common.by import By


class PicturePage:
    first_category = dict(by=By.CLASS_NAME, value="PopularRequestList-Item_pos_0")
    search_field = dict(by=By.CLASS_NAME, value="input__control.mini-suggest__input")
    first_image = dict(by=By.CLASS_NAME, value="serp-item_pos_0")
    opened_image = dict(by=By.CLASS_NAME, value="MMImage-Origin")
    next_image = dict(by=By.CLASS_NAME, value="CircleButton_type_next")
    previous_image = dict(by=By.CLASS_NAME, value="CircleButton_type_prev")
