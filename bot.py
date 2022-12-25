import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.config import load_config

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tg_bot.filters.admin import AdminFilter
from tg_bot.filters.admins import AdminsFilter
from tg_bot.filters.group_chat import IsGroup
from tg_bot.filters.moderate_chat import moderate_chat
from tg_bot.handlers.admin import register_admin
from tg_bot.handlers.catch_media import register_catch_media
from tg_bot.handlers.echo import register_echo
from tg_bot.handlers.edit_chat import edit_chat
from tg_bot.handlers.error_handler import register_errors_handler
from tg_bot.handlers.menu import register_menu
from tg_bot.handlers.new_post import register_new_post
from tg_bot.handlers.pop import register_pop
from tg_bot.handlers.poster import register_poster
from tg_bot.handlers.promotion import register_promotion
from tg_bot.handlers.purchase import register_show_items
from tg_bot.handlers.sending_cats import sending_cats
from tg_bot.handlers.service_messanges import register_service_messanges
from tg_bot.midelwares.big_brother import BigBrother
from tg_bot.midelwares.db import DdMiddleware
from tg_bot.midelwares.throttling import ThrottlingMiddlewares
from tg_bot.misc.states import register_test_q
from user.get_contact import get_contact_fail
from user.get_location import get_location_fail

logger = logging.getLogger(__name__)

def register_all_middlewares(dp):
    dp.setup_middleware(DdMiddleware())
    dp.setup_middleware(BigBrother())
    dp.setup_middleware(ThrottlingMiddlewares())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(AdminsFilter)
    dp.filters_factory.bind(IsGroup)

def register_all_handlers(dp):
    #register_catch_media(dp)
    sending_cats(dp)
    get_location_fail(dp)
    get_contact_fail(dp)
    register_errors_handler(dp)
    moderate_chat(dp)
    register_new_post(dp)
    register_poster(dp)
    register_admin(dp)
    register_promotion(dp)
    edit_chat(dp)
    register_pop(dp)
    register_test_q(dp)
    register_menu(dp)
    register_show_items(dp)
    register_service_messanges(dp)
    #register_echo(dp)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s,'
    )
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token,parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    from tg_bot.misc.utils.set_bot_commands import set_default_commands
    await set_default_commands(bot)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

