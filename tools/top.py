import time
import requests
import colorama
from colorama import Fore
import os


os.system("clear")

colorama.init()
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}

print ("Функция в бета версии!!!!")
print (Fore.YELLOW + "")

url = input("[+] URL VIDEO>")


view = input("[+] Кол-во Ботов:")

#script


for i in range(int(view)):
    time.sleep(0.10)
    bot = requests.get(url, headers=headers)
    
    if bot.status_code == 200:
        print (Fore.GREEN + "[+] Запрос успешный")
    else:
        print ("Ошибка запроса")

i = input("Нацжмите Enter")
os.system("clear")
os.system("python3 LIK.py")

