import time
import requests
#import random
import colorama
from colorama import Fore
import os

colorama.init()


#ok

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


info = """
Developer> RESHETKA
TELEGRAMM> NETY
----------------------------

ДАННЫЙ СОФТ СДЕЛАН ДЛЯ ПРИЛОЖЕНИЯ LIKEE!!!
"""



menu = """
[=] Developer: RESHETKA
------------------------------------------------
{+} 1. Скачать видео
{+} 2. Информация о трансляции
{+} 3. Информация о видео
{+} 4. Продвижение в рекомендации
{+} 5. Информация о софте
------------------------------------------------
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

if us =="5":
        print (Fore.BLUE + info)
        i = input("Нажмите Enter")
        os.system("clear")
        os.system("python3 LIK.py")

else:
    print ("Выход из программы...")
    time.sleep(1)
    exit()

#the end
        







#time.sleep(90)



















