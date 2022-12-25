from aiogram import types, Dispatcher

from tg_bot.filters.group_chat import IsGroup


async  def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Privet,{message.new_chat_members[0].full_name}.")

async def banned_member(message: types.Message):
    bot = message.bot
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} vishel iz chata")

    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} bil udalen iz chata"
                             f" polzovatelem{message.from_user.get_mention(as_html=True)}.")

def register_service_messanges(dp: Dispatcher):
    print("service_messanges")
    dp.register_message_handler(new_member, IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(banned_member, IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)