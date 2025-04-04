#import re
import requests
import os
import colorama
from colorama import Fore
import os
#import

colorama.init()


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
#scriptq


print (Fore.RED + "Чтобы получить информацию о видео вставьте url нижe")
print (Fore.YELLOW + "")


url = input("[+] URL VIDEO>")

print ("{=} Ищем данные...")
res = requests.get(url, headers=headers)
#  print (res.text)
import time
#time.sleep(909)

import re

data = (res.text)
#import re


translations = {
    "@context": "Контекст",
    "@type": "Тип",
    "name": "Имя",
    "description": "Описание",
    "thumbnailUrl": "URL превью",
    "contentUrl": "URL контента",
    "commentCount": "Количество комментариев",
    "uploadDate": "Дата загрузки",
    "duration": "Длительность",
    "width": "Ширина",
    "height": "Высота",
    "mainEntityOfPage": "Главная сущность страницы",
    "author": "Автор",
    "alternateName": "Альтернативное имя",
    "@id": "ID",
    "position": "Позиция",
    "item": "Элемент",
    "itemListElement": "Список элементов",
    "seoUrl": "SEO URL",
    "domain": "Домен",
    "title": "Заголовок",
    "url": "URL"
}

def extract_json_like_data(data):
    """Extracts and translates JSON-like data from a larger text."""
    data_dict = {}
    lines = data.splitlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().replace('"', '').replace('{','').replace('[','').replace('}','').replace(']','')
            value = value.strip().replace('"', '').replace('{','').replace('[','').replace('}','').replace(']','').replace(',','')

            if key in translations:
                translated_key = translations[key]
                data_dict[translated_key] = value

    return data_dict

extracted_data = extract_json_like_data(data)

# Print the extracted dёкata in a column format with translations
for key, value in extracted_data.items():
    print(f"{key}: {value}")
#the end reshetka

#import os
i = input("Нажите Enter")

os.system("clear")
os.system("python3 LIK.py")
time.sleep(3)



