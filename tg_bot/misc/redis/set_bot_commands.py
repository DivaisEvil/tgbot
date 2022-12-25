from aiogram import types, Dispatcher


async def set_default_commands(dp):
    bot = dp.bot
    await dp.bot.set_my_commands([
        types.BotCommand('chnnels', 'Spisok kanalov na podpisku'),
        types.BotCommand('create_post', 'Predlogit post v kanal')
    ])