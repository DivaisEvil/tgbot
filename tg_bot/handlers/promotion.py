from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery

from tg_bot.config import channels
from tg_bot.filters.forwarded_message import IsForwarded
from tg_bot.keybords.inline.subscription import check_button
from tg_bot.misc import subscription
from aiogram.dispatcher.filters import Command


async def get_channel_info(message: types.Message):    #(IsForwarded(), content_types =types.ChatType.ANY)
    await message.answer(f"Soobshenie prislano na canal iz canala {message.forward_from_chat.title}.\n"
                         f"Username: @{message.forward_from_chat.username}\n"
                         f"ID{message.forward_from_chat.id}")


async def show_channels(message: types.Message):
    print('show_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channelsshow_channels')
    bot = message.bot
    channels_format = str()
    for channel_id_or_username in channels:
        chat = await bot.get_chat(channel_id_or_username)
        invaite_link = await chat.export_invite_link()
        channels_format += f" Kanal <a href= '{invaite_link}'>{chat.title}</a>\n\n"
    await message.answer(f"Vam nado podpisatsa na kanali: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True
                         )
async def checker(call: CallbackQuery):
    bot = call.bot
    await call.answer()
    result = str()
    for channel in channels:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            # invite_link = await channel.export_invite_link()
            result += f"Podpis na kanal <b>{channel.title}</b> oformlena! Отлично"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"Podpis na kanal <b>{channel.title}</b> NE oformlena!"
                      f"<a href='{invite_link}'> Nado podpisatsa </a>\n\n")
    await call.message.answer(result, disable_web_page_preview=True)

def register_promotion(dp: Dispatcher):
    print("register promotion")
    dp.register_message_handler(get_channel_info, IsForwarded(), content_types =types.ContentType.ANY)
    dp.register_message_handler(show_channels, Command('channels', prefixes='!/'))
    dp.register_callback_query_handler(checker, text='check_subs')
