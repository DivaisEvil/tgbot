from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove


from tg_bot.keybords.menu import menu


async def show_menu(message: types.Message):
    await message.answer('Выберeте товар из меню ниже', reply_markup=menu)

async def get_Kotleti(message: types.Message):
    await message.answer('Vi vibrali Kotleti')

async def get_food(message: types.Message):
    print(message.text)
    await message.answer(f" Vi vibrali: {message.text}", reply_markup=ReplyKeyboardRemove())



def register_menu(dp: Dispatcher):
    print("register menu")
    dp.register_message_handler(show_menu, commands=['menu']),
    dp.register_message_handler(get_Kotleti, text='Kotleti'),
    dp.register_message_handler(get_food, Text(equals=['pure', 'spagetti']))
    print('register_menu PROVERKA')