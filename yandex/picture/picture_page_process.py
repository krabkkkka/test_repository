"""
Файл с описанием основных элементов страницы "Картинки"
"""
from selenium.webdriver.common.by import By


class PicturePageProcess:
    # Категории (первая в списке)
    first_category = dict(by=By.CLASS_NAME, value='PopularRequestList-Item_pos_0')
    # Поле поиска в картинках (возможно подойдет из страницы поиска)
    search_field = dict(by=By.CLASS_NAME, value='input__control.mini-suggest__input')
    # Первое изображение на открытие
    first_image = dict(by=By.CLASS_NAME, value='serp-item_pos_0')
    # src первого изображения
    src_first_image = dict(by=By.CLASS_NAME, value='MMImage-Origin')
    # src следующего изображения
    src_next_image = dict(by=By.CLASS_NAME, value='MMImage-Origin')
    # Кнопка следующее изображение
    next_image = dict(by=By.CLASS_NAME, value='CircleButton_type_next')
    # Кнопка предыдущее изображение
    previous_image = dict(by=By.CLASS_NAME, value='CircleButton_type_prev')

