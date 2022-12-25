from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="телефон",
                       request_contact=True)
        ]
    ],
     resize_keyboard=True
)