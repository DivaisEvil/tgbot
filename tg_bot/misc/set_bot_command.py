from aiogram import types


async def set_defaul_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('set_photo', 'Ustanovit foto v chate'),
        types.BotCommand('set_title', 'Ustanovit nazvanie grupi'),
        types.BotCommand('set_decsription', 'Ustanovit opisanie grupi'),
        types.BotCommand('ro', 'regim Read Only'),
        types.BotCommand('unro', 'otcluchit RO'),
        types.BotCommand('ban', 'zabanit'),
        types.BotCommand('unban', 'razbanit'),
    ])