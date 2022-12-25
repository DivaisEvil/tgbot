from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from tg_bot.config import admins, channels
from tg_bot.keybords.inline.callback_datas import buy_callback
from tg_bot.keybords.inline.manage_post import confirmation_keyboard, post_callback
from tg_bot.misc.poster import NewPost


async def create_post(massage: types.Message):
    print('create_postcreate_postcreate_postcreate_postcreate_postcreate_postcreate_postcreate_postcreate_post')
    await massage.answer('Otpravte mne post na publikaciu')
    await NewPost.EnterMessage.set()


async def enter_message(message: types.Message, state: FSMContext):
    print(
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    await  state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer('Vi sobiraetes otpravit post na proverku', reply_markup=confirmation_keyboard)
    await NewPost.next()


async def confirm_post(call: CallbackQuery, state: FSMContext):
    print('confirm_postconfirm_postconfirm_postconfirm_postconfirm_postconfirm_postconfirm_postconfirm_post')
    print(call.data)
    bot = call.bot
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await  state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Vi otpravili post na provercu')
    await bot.send_message(chat_id=admins[0], text=f"Polzovatel {mention} Hochet sdelat post")
    await bot.send_message(chat_id=admins[0], text=text, parse_mode="HTML", reply_markup=confirmation_keyboard)


async def cancel_post(call: CallbackQuery, state=FSMContext):
    print('cancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_postcancel_post')
    print(call.data)
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Vi otmenili post')


async def _post_unknown(message: types.Message):
    await message.answer('viberite opublicovat ili otklonit post')


async def approve_post(call: CallbackQuery):
    await call.answer('Vi odobrili post', show_alert=True)
    target_channel = channels[0]
    message = await  call.message.edit_reply_markup()
    await  message.send_copy(chat_id=target_channel)


async def decline_post(call: CallbackQuery):
    await call.answer('Vi otklonili post', show_alert=True)
    await call.message.edit_reply_markup()


def register_poster(dp: Dispatcher):
    print("register_poster")
    dp.register_message_handler(create_post, Command('create_post', prefixes='!/'))
    dp.register_message_handler(enter_message, state=NewPost.EnterMessage)
    dp.register_message_handler(_post_unknown, state=NewPost.Confirm)
    dp.register_callback_query_handler(confirm_post, post_callback.filter(action='post'),state=NewPost.Confirm)
    dp.register_callback_query_handler(cancel_post, post_callback.filter(action='cancel'),state=NewPost.Confirm)
    dp.register_callback_query_handler(approve_post, post_callback.filter(action='post'), user_id=admins)
    dp.register_callback_query_handler(decline_post, post_callback.filter(action='cancel'), user_id=admins)
