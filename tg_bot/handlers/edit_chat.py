import io

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from tg_bot.filters.admins import AdminsFilter
from tg_bot.filters.group_chat import IsGroup


async def set_new_photo(message: types.Message):
    bot = message.bot
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await  photo.download(destination=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    # await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    await message.chat.set_photo(photo=input_file)


async def set_new_title(message: types.Message):
    bot = message.bot
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title)

async def set_new_description(message: types.Message):
    bot = message.bot
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description)


def edit_chat(dp: Dispatcher):
    print("edit_chat")
    #dp.register_message_handler(set_new_photo, text = 'set_photo')
    dp.register_message_handler(set_new_photo, AdminsFilter(), IsGroup(),  Command('set_photo', prefixes='!/'))
    dp.register_message_handler(set_new_title, AdminsFilter(), IsGroup(),  Command('set_title', prefixes='!/'))
    dp.register_message_handler(set_new_description, AdminsFilter(), IsGroup(),  Command('set_description', prefixes='!/'))
