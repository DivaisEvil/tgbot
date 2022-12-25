from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class AdminsFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        print('AdminsFilterAdminsFilterAdminsFilterAdminsFilterAdminsFilterAdminsFilterAdminsFilterAdminsFilterAdminsFilter')
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()