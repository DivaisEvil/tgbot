from aiogram import Dispatcher
from aiogram.types import ContentType, Message, InputFile, MediaGroup

async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)

async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)

async def send_cat(message: Message):
    bot = message.bot
    photo_file_id = 'FILE ID = AgACAgQAAxkBAAIGmGNLQcnhM_qFTtptj5r-g5VbKCGaAAK3rjEb-0FsUu9K3qtaaaISAQADAgADdwADKgQ'
    photo_url = '...'
    photo_bytes = InputFile(path_or_bytesio='photo/cat.jpg')
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://kartinkin.net/uploads/posts/2022-01/1641926023_49-kartinkin-net-p-kotik-kosmonavt-art-krasivo-50.jpg',
                         caption='Vot tebe foto kota /more_cats')
    await message.answer_video('BAACAgIAAxkBAAIGoWNLQzfXwfWccvzFN2mY9vW15p7OAAJTGwAC8LaISfnk7ZF9eeIAASoE')

async  def more_cats(message: Message):
    bot=message.bot
    album = MediaGroup()
    photo_file_id = 'AgACAgQAAxkBAAIGmGNLQcnhM_qFTtptj5r-g5VbKCGaAAK3rjEb-0FsUu9K3qtaaaISAQADAgADdwADKgQ'
    photo_url = 'https://kartinkin.net/uploads/posts/2022-01/1641926023_49-kartinkin-net-p-kotik-kosmonavt-art-krasivo-50.jpg'
    photo_bytes = InputFile(path_or_bytesio='photo/cat.jpg')
    video_file_id = 'BAACAgIAAxkBAAIGoWNLQzfXwfWccvzFN2mY9vW15p7OAAJTGwAC8LaISfnk7ZF9eeIAASoE'
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_bytes)
    album.attach_photo(photo_url)
    album.attach_video(video_file_id,caption='Video kot prigaet' )


    #await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)


def sending_cats(dp: Dispatcher):
    print("register_sending_cats")
    dp.register_message_handler(get_file_id_p, content_types=ContentType.PHOTO)
    dp.register_message_handler(get_file_id_v, content_types=ContentType.VIDEO)
    dp.register_message_handler(send_cat, commands='get_cat')
    dp.register_message_handler(more_cats, commands='more_cats')