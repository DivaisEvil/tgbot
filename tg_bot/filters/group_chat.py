from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        print('IsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroupIsGroup')
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPER_GROUP,
        )