from aiogram import types, Dispatcher
from  aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import quote_html

from tg_bot.misc.utils import location_buttons
#from  loader import dp
from tg_bot.misc.utils.calc_distance import choose_shortest


async def show_on_map(message: types.Message):
    await message.answer(
        f" Hello, {message.from_user.full_name}.\n"
        f" Dla togo chtobi pokazat magaz radom, itpravte svoj lokaciu"
        f"nagav na comandu nige",
        reply_markup=location_buttons.keyboard
    )

async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    lonqitude = location.longitude
    closest_shops = choose_shortest(location)

    text_format = "nazvanie: {shop_name}. <a href='{url}'>Google</a>\n Rastojanie{distance:.1f} km"
    text = "\n\n".join(
        [
            text_format.format(shop_name=shop_name, url=url, distance = distance)
            for  shop_name, distance, url, shop_location in closest_shops
            
        ]
    )
    text1 = quote_html(f" Spasibo \n"
                       f" Latitude = {latitude}\n"
                       f"lonqitude = {lonqitude}\n\n"
                       f"{text}")
    print(text1)
    await message.answer(f" Spasibo \n"
                         f" Latitude = {latitude}\n"
                         f"lonqitude = {lonqitude}\n\n"
                         f"{text}",
                         disable_web_page_preview=True
                         )


    for shop_name, distance, url, shop_location in closest_shops:
        await  message.answer_location(latitude=shop_location["lat"], longitude=shop_location["lon"],)


def get_location_fail(dp: Dispatcher):
    print("get_location")
    dp.register_message_handler(show_on_map, commands=['show_on_map'])
    dp.register_message_handler(get_location, content_types=types.ContentType.LOCATION)
print(get_location)