#v04


import time
#import requests
import os

os.system("clear")

inst = """
+ ЭТОТ СКРИПТ ЗАПУСТИТ СЕРВЕР В ЛОКАЛЬНОЙ СЕТИ
+ ВЫ МОЖЕТЕ ВСТАВЛЯТЬ СВОИ HTML СКРИПТЫ
"""

time.sleep(1)
menu = """
1) Start Server
2) Exit
"""
print (menu)
us = input("[=] Выбирай>")

if us == "1":
    print ("Запуск Сервера...")
    os.system("python -m http.server")
    print ("Server запущен!")
    #start server
else:
    print ("Закрываю программу")
    exit()

#the end


















































