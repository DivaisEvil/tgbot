# 'состояния дляпубликации постов hendler poster'

from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
    EnterMessage = State()
    Confirm = State()