from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot.keybords.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,#row_width kolichestvo knopok v stroke
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='kupi grushu',
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity=1)
                                      ),
                                     InlineKeyboardButton(
                                         text='kupi jabloki',
                                         callback_data='buy:apple:5'
                                     )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='otmena',
                                          callback_data='cancel'
                                      )
                                  ],
                              ])

pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = 'HTTPS://YANDEX.RU/USSR'

pear_link = InlineKeyboardButton(text='kupi tut', url=PEAR_LINK)

pear_keyboard.insert(pear_link)