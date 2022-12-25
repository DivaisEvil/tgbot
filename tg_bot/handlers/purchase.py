import logging
from unittest.mock import call

from  aiogram.dispatcher.filters import  Command
from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery

from tg_bot.keybords.inline.callback_datas import buy_callback
from tg_bot.keybords.inline.choice_buttons import choice, pear_keyboard


async def show_items(message: types.Message):
    await  message.answer(text='Na prodagu u nas est 2 tovara: 5 jablok i 1 grusha\n'
                         ' Esli net, otmeni',
                            reply_markup=choice)

async def buying_pear(call: CallbackQuery, callback_data: dict):
    #await bot.answer_callback_query(callback_query_id=call.id)
    #await call.answer() убирают часики при нажатии на кнопки
    print('222222222222222222222222222222222222222222222222222222222222222')
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get('quantity')
    await call.message.answer(f"vi vibroli kupit grushu. Grush vsego {quantity}. Spasibo",
                              reply_markup=pear_keyboard)

async def buying_aplle(call: CallbackQuery, callback_data: dict):
    print('111111111111111111111111111111111111111')
    #await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get('quantity')
    await call.message.answer(f"vi vibroli kupit jabloki. jablok vsego {quantity}. Spasibo")

async def cancel(call: CallbackQuery):
    print('cancel')
    #await call.answer(cache_time=60)
    await call.answer('Vi otmenili', show_alert=True)
    await call.message.edit_reply_markup()


def register_show_items(dp: Dispatcher):
    print("register_show_items")
    dp.register_message_handler(show_items, commands=['items'])
    dp.register_callback_query_handler(buying_pear, buy_callback.filter(item_name='pear'))
    dp.register_callback_query_handler(buying_aplle, buy_callback.filter(item_name='apple'))
    dp.register_callback_query_handler(cancel, text='cancel')
    #dp.register_callback_query_handler(ccancel, buy_callback.filter(item_name='cancel'))
    #dp.register_callback_query_handler(buying_aplle, buy_callback.filter(item_name='aplle'))