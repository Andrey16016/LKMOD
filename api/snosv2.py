#SETINGS
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
bots = "1"
valid = '{"code":0,"data":{"success":true,"receipt":null},"message":"ok"}'
#-----
print ("")

import time
import requests
import os
import json
import secrets, string
import random
import colorama
from colorama import Fore
import re

colorama.init()
os.system("clear")

print (Fore.GREEN + "")
logo = """
╭━━━┳╮╱╱╭┳━━━━┳━━━┳━━━┳━╮╱╭┳━━━┳━━━╮
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃╭━╮┃╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
┃┃╱┃┣╮┃┃╭┻╯┃┃╰┫┃╱┃┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
┃╰━╯┃┃╰╯┃╱╱┃┃╱┃┃╱┃┣━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
┃╭━╮┃╰╮╭╯╱╱┃┃╱┃╰━╯┃╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰╯╱╰╯╱╰╯╱╱╱╰╯╱╰━━━┻━━━┻╯╱╰━┻━━━┻━━━╯
"""
print (logo)


url = "https://d2v9yioq9zuuq2.cloudfront.net/passthroush/live-api.likee.com/likee-bs-flow-client/accusation/submitSceneReport"
user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"
#x_auth_token = "YOUR_X_AUTH_TOKEN"

menu = """
1) Отправка жалоб по Cсылке
2) Отправка жалоб по POST ID
"""
print (Fore.YELLOW + menu)

user = input("Выбирай>")
if user == "2":
    os.system("clear")
    print ("")
    print ("Вставьте POST ID видео ниже!")
    video = input("POST ID>")
    os.system("clear")
    print (f"Атака на {video}")
else:
    os.system("clear")
    print ("")
    print ("Вставьте ссылку на видео")
    urlv = input("URL VIDEO>")
    print (f"Запуск сноса...")
    line = requests.get(urlv, headers=headers)
    code_example = (line.text)
    match_post = re.search(r'"post_id":\s*"([^"]*)"', code_example)
    match_nick = re.search(r'"nick_name":\s*"([^"]*)"', code_example)
    share_post = match_post.group(1)
    share_nick = match_nick.group(1)
    video = (share_post)
    info = f"""
    [+] Запуск атаки на <{share_nick}>
    [+] ID видео {share_post}
    [+] 60 Жалоб
    """
    print (Fore.GREEN + info)
    
    


#7527666538050399162
#information support


x_auth_token = input("Введите токен>")

device_id = ''.join(secrets.choice(string.hexdigits.lower()) for _ in range(40))

with open("suport.txt", 'r', encoding='utf-8') as f:
    texts = f.readlines()
    suport = (random.choice(texts).strip())

data_json = {"description": suport, "attachments": []}

data1 = {
    "deviceId": device_id,
    "language": "ru",
    "id": "10002",
    "reason": "Безопасность несовершеннолетних",
    "tagId": "",
    "tagName": "",
    "reportedId": video,
    "dataJson": "{\"description\":\"Плохое поведение людей в обществе\",\"attachments\":[]}"
}

data2 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10006",
  "reason": "Порнография или нагота",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"В видео показано порно с несовершеннолетними детьми!\",\"attachments\":[]}"
}



data3 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10009",
  "reason": "Запрещённые предметы",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"В видео показаны наркотики, оружие, расчлененка, ножи.\",\"attachments\":[]}"
}

data4 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10011",
  "reason": "Прочее",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": json.dumps(data_json, ensure_ascii=False)
}

data5 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10001",
  "reason": "Ложная информация",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"Распространение ложной информации  в видеороликах, прошу принять меры.\",\"attachments\":[]}"
}

data6 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10003",
  "reason": "Оскорбительный или издевающийся",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"Оскорбления в сторону людей, примите меры!\",\"attachments\":[]}"
}



data7 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10005",
  "reason": "Недопустимый политический или религиозный контент",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"Террористическая деятельность, оскорбление религии!\",\"attachments\":[]}"
}





headers = {
    'Content-type': 'application/json',
    'User-Agent': user_agent,
    'X-Auth-Token': x_auth_token,
    'Accept-Language': 'ru'
}


os.system("clear")
res = requests.post(url, data=json.dumps(data1), headers=headers)
if res.text == valid:
    print ("Успешно")
else:
    print ("")
    print ("Токен устарел")
    time.sleep(1.10)
    os.system("clear")
    os.system("python3 LIK.py")
    exit()
    #the end
    
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data2), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data3), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data4), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data5), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data6), headers=headers)
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data7), headers=headers)
print (res.text)
time.sleep(1)








#script



print ("Все жалобы отправлены!")
print ("")
i = input("Нажмите Enter")
os.system("clear")
os.system("python3 LIK.py")
#the end
    




