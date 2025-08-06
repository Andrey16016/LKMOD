import requests
import time
import colorama
from colorama import Fore



import os

os.system("clear")

colorama.init()
print (Fore.RED + "Скопируйте URL трансляции и вставьте!!!")
time.sleep(1)

print (Fore.YELLOW + "")
url = input("[+] URL ТРАНСЛЯЦИИ>")
print ("{=} Получаем информацию...")

res = requests.get(url)
data = (res.text)

import re
#qsc
print ("Данные:")


#script
translations = {
    "app_urlp": "URL приложения",
    "buuid": "BUUID",
    "profile_id": "ID профиля",
    "appStore_url": "URL App Store",
    "googlePlay_url": "URL Google Play",
    "lang": "Язык",
    "nick_name": "Никнейм",
    "user_name": "Имя пользователя",
    "share_avatar": "Аватар для шаринга",
    "share_nick": "Никнейм для шаринга",
    "share_post_wechat_desc": "Описание для шаринга в WeChat",
        "share_user_invited_title": "Приглашение пользователя в шаринге",
    "share_open_app": "Открыть в приложении",
    "user_replay": "Повтор",
    "share_record": "Записывать",
    "sideUp_more": "Свайп вверх для большего",
    "user_follow": "Подписаться",
    "LIKE_ID_TITLE": "Likee ID",
    "today_hot": "Популярные сегодня",
    "more_live_LIke": "Больше волшебных видео в LIKE App",
    "share_bottom_join_lang_img": "Язык изображения для присоединения внизу шаринга",
    "share_bottom_join_btn": "Присоединиться",
    "modal_download_tips": "Загрузите Likee, чтобы связаться с этим лайкером",
    "modal_download_ok": "ОК",
    "modal_download_cancel": "Отмена",
    "videoTips": "Подпишитесь на лайкера в Likee и вы не пропустите следующее шоу",
    "live_ended": "Трансляция завершена",
    "live_tips": "Общайся с Лайкером сейчас",
    "share_tips": "Текст для шаринга",
    "live_num": "Количество зрителей",
    "video_url": "URL видео",
    "video_poster": "URL обложки видео",
    "video_width": "Ширина видео",
    "video_height": "Высота видео",
    "user_avatar": "URL аватара пользователя",
    "title": "Заголовок",
    "desc": "Описание",
    "wsUrl": "URL WebSocket",
    "roomId": "ID комнаты",
}

# Create a set of valid keys for parsing
valid_keys = set(translations.keys())


data_dict = {}

for line in data.splitlines():
    line = line.strip()
    if not line:
        continue

    # Remove comments
    line = re.sub(r'\/\*.*?\*\/', '', line).strip()

    if '=' in line:
        key, value = line.split('=', 1)
        key = key.strip()

        # Check if the key is in the list of keys to be parsed
        if key in valid_keys:
            value = value.strip().rstrip(',')  # Remove trailing comma

            # Remove quotes and handle potential issues with quotes in the values
            if value.startswith("'") or value.startswith('"'):
                value = value[1:-1]
            
            data_dict[key] = value

# Print in a column format with translations
for key, value in data_dict.items():
    translated_key = translations.get(key, key)  # Use the original key if no translation is found
    print(f"{translated_key}: {value}")
    time.sleep(0.05)

i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIK.py")
