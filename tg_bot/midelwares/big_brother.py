import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from tg_bot.config import banned_users


class BigBrother(BaseMiddleware):
    #1
    async def on_pre_process_update(self, update: types.Update, data :dict):
        logging.info("[-------------------- NEW APDEITS------------------]")
        logging.info("1. Pre Process Update")
        logging.info("Nex dot: Process Update")
        data["middleware_data"] = "Это пройдет до on_post_process_update"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user in banned_users:
            raise CancelHandler()
#2
async def on_process_update(self, update: types.Update, data: dict):
    logging.info(f"2. Process Update, {data=}")
    logging.info("New dot: Pre Process Massage")

#3
async  def on_pre_process_message(self, message: types.Message, data: dict):
    logging.info(f"3. Pre Process Message, {data=}")
    logging.info("New dot: Filters, Process Message")
    data["middleware_data"] = "This going of on_process_message"

#4 Filters

#5
async def on_prosecc_message(self, message: types.Message, data:dict):
    logging.info(f"5. Process Message")
    logging.info("next dot: Handler")

#6 Handler

#7
async def on_post_process_message(self, message: types.Message, data_from_filter: list, data:dict):
    logging.info(f"7. Post ProcessMessage, {data=}, {data_from_filter}")
    logging.info("next dot, Post Process Update")

#8
async def on_post_process_update(self, update: types.Update, data_from_handler:list, data: dict):
    logging.info(f"8. Post Process Update, {data=}, {data_from_handler=}")
    logging.info(f"[--------------------Exit--------------------------]\n")


async  def on_pre_process_callback_query(self, cq: types.CallbackQuery, data: dict):
    await cq.answer()