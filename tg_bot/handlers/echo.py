from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import state
from aiogram.utils.markdown import hcode


async  def bot_echo(message: types.Message):
    text = [
        "Эхо",
        "Сообщение",
        message.text
    ]
    await  message.answer('\n'.join(text))

async  def bot_echo_all (message: types.Message):
    state_name = await state.get_state()
    text = [
        f"Эхо {hcode(state_name)}",
        "Сообщение",
        message.text
    ]
    await  message.answer('\n'.join(text))

def register_echo(dp: Dispatcher):
    print("register echo")
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo, state='*',content_types=types.ContentType.ANY)

