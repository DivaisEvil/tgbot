import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

async def new_post(message: types.Message):
    logging.info(f"Opublikovano new post {message.chat.title}.\n"
                 f"{message.text}")


def register_new_post(dp: Dispatcher):
    print("new_post")
    dp.register_channel_post_handler(new_post, content_types=types.ContentType.ANY)
    #dp.register_channel_post_handler()