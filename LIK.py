#SETINGS
server = "https://bstream.likeeapp.ru/json?uri=8001001&aid=48&t=0.7859116550012502"
txt = 'Добро Пожаловать! Данный софт был написан исключительно в ознакомительных целях, мы не отвечаем за ваши действия!'





#CODE
print ("Loading...")


import time
import requests
#import random
import colorama
from colorama import Fore
import os

colorama.init()
os.system("clear")
print (Fore.YELLOW + "")


with open('keysoft.txt', 'r', encoding='utf-8') as file:
    for line in file:
        key = (line.strip())
        
        #print (key)
res = requests.get(server)

if key == (res.text):
    #print ("Доступ разрешен!")
    os.system("clear")
else:
    for i in txt:
        time.sleep(0.04)
        print(i, end='', flush=True)
    #ввод ключа
    print ("")
    new = input("Введи Ключ Доступа:")
    if new == (res.text):
        with open('keysoft.txt', 'w', encoding='utf-8') as file:
            file.write(res.text)
            #the end
    else:
        print ("Ключ не верный!")
        print ("Закрываем программу")
        time.sleep(1)
        os.system("clear")
        exit()





#info
vers = "0.05"
update = "Исправление ошибок, добавление новых функций."


os.system("clear")






#command


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


info = f"""
Developer> (RESHETKA), RAZVEDKA
----------------------------

Версия> {vers}
ДАННЫЙ СОФТ СДЕЛАН ДЛЯ ВЗАИМОДЕЙСТВИЯ С LIKEE!

ОБНОВЛЕНИЕ 29.07.2025

{update}

"""



menu = """
[=] Developer: RESHETKA, RAZVEDKA
--------------------------------------------
{+} 1. Скачать видео
{+} 2. Информация о трансляции
{+} 3. Информация о видео
{+} 4. Продвижение в рекомендации
{+} 5. Информация о софте
{+} 6. Snosing
{+} 7. Поиск по username
{+} 8. Данные о видео из аккаунта
{+} 9. Информация об аккаунте


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

if us == "8":
    from api import videoapi

if us == "7":
    from tools import search

if us == "9":
    from api import probiv


    


    

if us =="5":
    print (Fore.BLUE + "")
    os.system("clear")
    print("")
    for i in info:
        time.sleep(0.04)
        print(i, end='', flush=True)
    
        #print (Fore.BLUE + info)
    i = input("Нажмите Enter")
    os.system("clear")
    os.system("python3 LIK.py")

else:
    #script
    print ("Выход из программы...")
    time.sleep(1)
    exit()

#the end
        







#time.sleep(90)



















