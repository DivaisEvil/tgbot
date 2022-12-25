import math
from aiogram import types

from tg_bot.misc.utils import show_on_gmaps
from tg_bot.misc.utils.show_on_gmaps import show

from tg_bot.misc.data.locations import Shops

R = 6378.1

def calc_distance(lat1, lon1, lat2, lon2):
    # lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    # a = sin(dlat / 2)  2 + cos(lat1) * cos(lat2) * sin(dlon / 2)  2
    a = math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    # c = 2 * asin(sqrt(a))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    # Radius of earth in kilometers is 6371
    # km = 6371 * c
    # return ceil(km * 1000)
    print(distance)
    return distance


def choose_shortest(location: types.Location):
    distances = list()
    for shop_name, shop_location in Shops:
        distances.append((shop_name,
                          calc_distance(location.latitude, location.longitude,
                                        shop_location["lat"], shop_location["lon"]),
                          show_on_gmaps.show(**shop_location),
                          shop_location
                          ))
    return sorted(distances, key=lambda x: x[1])[:2]
