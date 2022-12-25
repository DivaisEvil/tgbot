from aiogram import types
async def set_default_commands(bot):
    #bot = dp.bot
    await bot.set_my_commands([
        types.BotCommand('get_cat', 'prislat kota'),
        types.BotCommand('more_cats', 'prislat bolshe kotikov')
    ])