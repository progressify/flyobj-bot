import json
import logging
from io import BytesIO
from typing import Dict, Optional

import requests
from PIL import Image
from telepot.namedtuple import KeyboardButton

import config
import pickle
from config import BASE_URL_RADAR, BASE_URL_MAPS, MAPS_KEY
from db_manager import DbManager


def get_flight_info(user_dict: Dict, txt: str) -> Optional[Dict]:
    volo = txt[3:-1]
    file_da_leggere = open(f"pickle/{user_dict['chat_id']}.pickle", "rb")
    dict_from_file = pickle.load(file_da_leggere)
    try:
        flight_dict = {
            'call': dict_from_file[volo]['Call'],
            'op': dict_from_file[volo]['Op'],
            'from': dict_from_file[volo].get('From'),
            'to': dict_from_file[volo]['To'],
            'hight': round((dict_from_file[volo]['GAlt']) * 0.3048),
            'speed': round((dict_from_file[volo]['Spd']) * 1.852),
            'trak': dict_from_file[volo]['Trak'],
            'velocita_cambio': round((dict_from_file[volo]['Vsi']) * 1.852)
        }

        return flight_dict
    except KeyError as e:
        logging.info('I got a KeyError - reason "%s"' % str(e))
        return None


def elenco_aerei(user_dict: Dict, latitudine, longitudine) -> Optional[Dict]:
    dict_from_file = dict()
    file_da_leggere = open(f"pickle/{user_dict['chat_id']}.pickle", "wb")

    db = DbManager()
    if db.has_quota_reached():
        return {
            'success': False,
            'message': "Limite chiamate mensile raggiunto.",
            'keyboard': [],
            'image': None,
        }
    else:
        url = config.RAPID_API_BASE_URL.format(lat=latitudine, lon=longitudine)
        headers = {
			'x-rapidapi-host': config.RAPID_API_HOST,
			'x-rapidapi-key': config.RADIP_API_KEY
		}
        with requests.get(url, headers=headers) as response:
            data = json.loads(response.text)
        db.increase_counter()

    elenco_aerei = []
    markers = ""
    a = 0
    for i in data[u'ac']:
        a += 1
        try:
            markers = f"{markers}&markers=color:red%7Clabel:{a}%7C{i['lat']},{i['lon']}"
            dict_from_file[i['call']] = i

            elenco_aerei.append(i['call'])
            logging.info('elenco aerei :' + str(elenco_aerei))
        except KeyError as e:
            logging.info('I got a KeyError - reason "%s"' % str(e))

    new_keyboard = []
    b = 0
    for aereo in elenco_aerei:
        b += 1
        new_keyboard.append([KeyboardButton(text=str(b) + ' >' + aereo + '<')])

    map_url = f"{BASE_URL_MAPS}?center={latitudine},{longitudine}&zoom=9&size=800x800&maptype=roadmap&{markers}" \
              f"&key={MAPS_KEY}"
    r = requests.get(map_url)
    image_name = f"maps/{user_dict['chat_id']}.png"
    mappa = Image.open(BytesIO(r.content))
    mappa.save(image_name)
    pickle.dump(dict_from_file, file_da_leggere)

    return {
        'success': True,
        'keyboard': new_keyboard,
        'image': image_name,
    }
