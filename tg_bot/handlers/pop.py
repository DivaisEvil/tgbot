from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import state
from aiogram.utils.markdown import hcode

from tg_bot.misc.throttling import rate_limit


@rate_limit(5, key='bot_pop')
async  def bot_pop(message):
    #text = 'ddd'

    text = 'pop super pop'
    await  message.answer(text)



def register_pop(dp: Dispatcher):
    print("register pop")
    dp.register_message_handler(bot_pop, state="*", regexp="^pop$")



