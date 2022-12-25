from aiogram import types, Dispatcher


async def catch_text(message: types.Message):
    await message.answer('Vi prislalr text')

async def catch_doc(message: types.Message):
    await message.answer('Vi prislalr document')
    await message.document.download()
    await message.reply('Document skachen\n'
                        f"<pre>FILE ID = {message.document.file_id}</pre>",
                        parse_mode="HTML")

async def catch_audio(message: types.Message):
    await message.answer('Vi prislalr audio')
    await message.audio.download()
    await message.reply('Audio skachen\n'
                        f"<pre>FILE ID = {message.audio.file_id}</pre>",
                        parse_mode="HTML")

async def catch_video(message: types.Message):
    await message.answer('Vi prislalr video')
    await message.video.download()
    await message.reply('Video skachen\n'
                        f"<pre>FILE ID = {message.video.file_id}</pre>",
                        parse_mode="HTML")

async def catch_photo(message: types.Message):
    await message.answer('Vi prislalr photo')
    await message.photo[-1].download()
    await message.reply('Photo skachen\n'
                        f"<pre>FILE ID = {message.photo[-1].file_id}</pre>",
                        parse_mode="HTML")

async def catch_any(message: types.Message):
    await message.answer(f"Vi prislalr {message.content_type}")

def register_catch_media(dp: Dispatcher):
    print("register_catch_media")
    dp.register_message_handler(catch_text, content_types=types.ContentType.TEXT)
    dp.register_message_handler(catch_doc, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(catch_audio, content_types=types.ContentType.AUDIO)
    dp.register_message_handler(catch_video, content_types=types.ContentType.VIDEO)
    dp.register_message_handler(catch_photo, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(catch_any, content_types=types.ContentType.ANY)
