import time
#import requests
import random
from random import randint
import colorama
from colorama import Fore


colorama.init()

print (Fore.GREEN + "")
import os

os.system("clear")



#scriptq
primer = """
= ЗАПРОС LKMOD
+ ДАННЫЕ НАЙДЕНЫ
= Пиложение (*LIKEE)

Ник: {name}
UserName: {user}
Ccылка на канал: {line}
Ip адрес: {ip}
Uuid phone: {id}
Mac адрес: {mac}
Index phone: {index}
Открытый Порт: {port}



"""


print ("FAKE GENERATOR")


print ("")
print ("Генератор OSINT Данных для Likee")

print ("")


name = input("[=] Введите Nikname>")
user = input("[=] Введите UserName>")
line = input("[=] Ccылка на Канал>")
server = input("[=] Cтрана:")

#ip adress
def generate_random_ip():
    return '.'.join(
        str(randint(0, 255)) for _ in range(4)
    )


random_ip = generate_random_ip()
#print(random_ip)

ip = (random_ip)

#id gener

ids = random.randint(11111111, 999999999999)

#index
index = random.randint(1000, 9999)
#mac adress

mac = 'MD:0F:3H:H0:6N'


#mac = (ms)

#port phone

port = random.randint(80, 3001)

#dox system
import random

hash = random.getrandbits(128)

key =  ("%032x" % hash)

#key =







#baza osint
text = f"""
= ЗАПРОС LKMOD
+ ДАННЫЕ НАЙДЕНЫ
= Пpиложение (*LIKEE)

Ник: {name}
UserName: {user}
Ccылка на канал: {line}
Ip адрес: {ip}
Uuid phone: {ids}
Mac адрес: {mac}
Index phone: {index}
Открытый Порт: {port}
Location: Неизвестно
User Server: {server}
Тип соединения: TCP
Зашифрованый ключ: {key}

+ Отчёт окончен +

"""

print (text)
#start script

i = input("Нажмите Enter")

os.system("clear")
os.system("python3 LIK.py")

#the end






























