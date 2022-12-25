from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import quote_html

from tg_bot.misc.utils import location_buttons
# from  loader import dp
from tg_bot.misc.utils.calc_distance import choose_shortest


async def share_number(message: types.Message):
    await message.answer(
        f" Hello, {message.from_user.full_name}.\n"
        f" Dla togo chtobi menedger perezvonil"
        f"nagav na comandu nige",
        reply_markup=location_buttons.keyboard
    )


async def get_contact(message: types.Message):
    contact = message.contact

    await message.answer(f" Spasibo {contact.full_name}\n"
                         f" Vash nomer {contact.phone_number}\n"
                         f"bil poluchen\n\n",
                         reply_markup=ReplyKeyboardRemove()
                         )

def get_contact_fail(dp: Dispatcher):
    print("get_contact")
    dp.register_message_handler(share_number, commands=['callback'])
    dp.register_message_handler(get_contact, content_types=types.ContentType.CONTACT)


print(get_contact)