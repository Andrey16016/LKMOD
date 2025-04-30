print ("Loading...")


import time
import requests
#import random
import colorama
from colorama import Fore
import os

colorama.init()

#info
vers = "0.04"
update = "Исправление ошибок, добавление новых функций."
#ok
##start = "python LIK.py"

os.system("clear")
print ("Проверка Cоединения с Likee")
r = requests.get("https://likee.com/")
if r.status_code == 200:
    print ("Соединение установлено")
    time.sleep(1)
    os.system("clear")
    
else:
    print ("Сервер не ответил!")
    print ("Закрываю Программу")
    exit()
    
    



#command


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


info = """
Developer> RESHETKA
TELEGRAMM> @h1user
----------------------------

ДАННЫЙ СОФТ СДЕЛАН ДЛЯ ПРИЛОЖЕНИЯ LIKEE!!!
"""



menu = """
[=] Developer: RESHETKA
--------------------------------------------
{+} 1. Скачать видео
{+} 2. Информация о трансляции
{+} 3. Информация о видео
{+} 4. Продвижение в рекомендации
{+} 5. Информация о софте
{+} 6. Snosing
[=] 0. Выход
--------------------------------------------
"""
#url = input("URL>")


with open("logo.txt", "r", encoding='utf-8') as file:
    logo = content = file.read()
    print (Fore.RED + logo)

print (Fore.YELLOW + menu)

#scripts

us = input("[+] Выбирай>")
#111

if us == "1":
    from tools import urlv

if us == "2":
    from tools import live

if us == "3":
    from tools import video

if us == "4":
    from tools import top

if us == "6":
    from tools import snoser

if us == "host":
    from tools import host
    

if us =="5":
        print (Fore.BLUE + info)
        print ("Версия софта:", vers)
        print ("Последнее обновление:")
        print (update)
        i = input("Нажмите Enter")
        os.system("clear")
        os.system("python3 LIK.py")

else:
    print ("Выход из программы...")
    time.sleep(1)
    exit()

#the end
        







#time.sleep(90)



















