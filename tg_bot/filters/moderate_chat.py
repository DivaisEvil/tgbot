import asyncio
import datetime
import re

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from tg_bot.filters.admins import AdminsFilter
from tg_bot.filters.group_chat import IsGroup


async def read_only_mode(message: types.Message):
    bot = message.bot
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+D ]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not  time:
        time = 5
    else:
        time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=True,
        can_pin_messages=False,
        can_change_info=False,

    )
    try:
        await bot.restrict_chat_member(chat_id, user_id=member_id, permissions=ReadOnlyPermissions, until_date=until_date)
        await message.reply(f"Polzovatelu {member.get_mention()} zapresheno pisat na {time} minut. Pricchina {comment}")
    except BadRequest:
        await message.answer("Polzovatel admin")
    except Exception as err:
        await message.answer(f"{err.__class__.__name__}: {err}")


    service_message = await message.reply('Message delite 5 secund')
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


async def undo_read_only_mode(message: types.Message):
    bot = message.bot
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_pin_messages=False,
        can_change_info=False,

    )

    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Polzovatel {member.full_name} bil razbanin")

async def ban_user(message: types.Message):
        bot = message.bot
        member = message.reply_to_message.from_user
        member_id = member.id
        chat_id = message.chat.id
        await  message.chat.kick(user_id=member_id)
        await message.reply(f"Polzovatel {member.full_name} bil zabanen")


async def unban_user(message: types.Message):
    bot = message.bot
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await  message.chat.unban(user_id=member_id)
    await message.reply(f"Polzovatel {member.full_name} bil razbanen")


def moderate_chat(dp: Dispatcher):
    print("moderate_chat")
    #dp.register_message_handler(set_new_photo, text = 'set_photo')
    dp.register_message_handler(read_only_mode, AdminsFilter(), IsGroup(),  Command('ro', prefixes='!/'))
    dp.register_message_handler(undo_read_only_mode, AdminsFilter(), IsGroup(),  Command('unro', prefixes='!/'))
    dp.register_message_handler(ban_user, AdminsFilter(), IsGroup(),  Command('ban', prefixes='!/'))
    dp.register_message_handler(unban_user, AdminsFilter(), IsGroup(),  Command('unban', prefixes='!/'))