import time
#import random
#import requests
import os
import colorama
from colorama import Fore

os.system("clear")

colorama.init()

body = """
SNOSING HELP
-----------
+ Поможет снести видео, Повесить блок на аккаунт +
"""


#print ("Поможет снести видео, посеть блок")
print (Fore.YELLOW + body)

#video install

##password = input("[=]Пароль:")

#soft
menu = """
Выберите жалобу
1) Ложная информация
2) Угрозы
3) 18+
4) Запрещенка
5) Просто SNOS
"""

print ("")
print (menu)
us = input("[*] Выбирай>")

#login




username = input("[=]Введите UserName>")


text = f"""
Hello, this account {username} violates the Likee rules. I ask you to pay attention and take action!
"""


if us == "1":
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + Ложная информация + Дезинформация + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")
    #the end

if us == "2":
    print ("ИНСТРУКЦИЯ")
    print ("Выбрать видео, Жалоба + Угроза личной безопасности + Оскорбление + В Описание вставить текст который ниже + Добавить 1 скрин")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")

if us == "3":
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + П#рн#гр#фия или наг##а + Открытая одежда + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")

if us == "4":
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + Запрещённые предметы + Огнестрел/ножи + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")

if us == "5":
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + Безопасность несовершеннолетних + Нанесение вреда... + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")
    


    



    
    

#print ("Ожидайте...")
           






