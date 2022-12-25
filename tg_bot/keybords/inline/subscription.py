from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Prover podpiski',
                                 callback_data='check_subs')
        ]
    ]
)