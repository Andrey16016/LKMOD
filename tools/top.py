import time
import requests
import colorama
from colorama import Fore
import os


os.system("clear")

colorama.init()
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/605.1 NAVER(inapp; search; 1010; 11.24.5; SE2)'}


#script

print ("Функция в бета версии!!!!")
print (Fore.YELLOW + "")

url = input("URL VIDEO>")
bots = input("Кол-во просмотров>")


for i in range(int(bots)):
    bot1 = requests.post(url, headers=headers)
    print (bot1.status_code)
#    bot2 = requests.post(url, headers=headers)
 #   print (bot2.status_code)
    
    time.sleep(0.10)
    #ok
    

print ("Программа окончила свою работу")
i = input("Нажмите Enter")
os.system("clear")
os.system("python3 LIK.py")

