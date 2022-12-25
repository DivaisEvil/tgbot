from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kotleti')
        ],
        [
            KeyboardButton(text='spagetti'),
            KeyboardButton(text='pure'),
        ],
    ],
    resize_keyboard=True
)