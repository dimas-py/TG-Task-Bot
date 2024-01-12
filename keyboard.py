from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.types.web_app_info import WebAppInfo


def create_main_keyboard(user_id, FLASK_URL):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Создать задачу",
                               web_app=WebAppInfo(url=f"{FLASK_URL}/?user_id={user_id}"))
            ],
            [
                KeyboardButton(text="Актуальные задачи", web_app=WebAppInfo(url=f'{FLASK_URL}/get_tasks?user_id={user_id}')),
                KeyboardButton(text="Выполненные задачи"),
            ],
            [
                KeyboardButton(text="Корзина")
            ],
            [
                KeyboardButton(text="Тест")
            ]
        ],
        resize_keyboard=True,  # маленькая клава
        one_time_keyboard=True,  # скрыть клаву после 1-ого нажатия
        input_field_placeholder="Выберите действие",  # инфа в поле ввода
        selective=True  # клава будет вызвана у того, кто её вызвал
    )
