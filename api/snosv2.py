#SETINGS
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
bots = "12"
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


device_id = ''.join(secrets.choice(string.hexdigits.lower()) for _ in range(40))



data1 = {
    "deviceId": device_id,
    "language": "ru",
    "id": "10002",
    "reason": "Безопасность несовершеннолетних",
    "tagId": "",
    "tagName": "",
    "reportedId": video,
    "dataJson": "{\"description\":\"\",\"attachments\":[]}"
}

data2 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10006",
  "reason": "Порнография или нагота",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"\",\"attachments\":[]}"
}



data3 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10009",
  "reason": "Запрещённые предметы",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"\",\"attachments\":[]}"
}

data4 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10011",
  "reason": "Прочее",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"Здравствуйте, данный аккаунт распространяет порнографию, ложную информацию, торгует наркотиками! Прошу срочно принять меры!\",\"attachments\":[]}"
}





#script

for i in range(int(bots)):
    filename = 'tokens.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        x_auth_token = (random.choice(f.readlines()).strip())

    headers = {
        'Content-type': 'application/json',
        'User-Agent': user_agent,
        'X-Auth-Token': x_auth_token
        }

    
    res = requests.post(url, data=json.dumps(data1), headers=headers)
    if res.text == valid:
        os.system("clear")
        print (f"+ Успешно + Поток> {i+1}")
    else:
        os.system("clear")
        print ("Ошибка, токены устарели")
        
    #print (res.text)
    time.sleep(1)
    res = requests.post(url, data=json.dumps(data2), headers=headers)
    print (res.text)
    time.sleep(1)
    res = requests.post(url, data=json.dumps(data3), headers=headers)
    #print (res.text)
    time.sleep(1)
    res = requests.post(url, data=json.dumps(data4), headers=headers)
    print(res.text)
    print ("Ожидпние следущего потока...")
    time.sleep(5)
    time.sleep(1)


print ("Все жалобы отправлены!")
print ("")
i = input("Нажмите Enter")
os.system("clear")
os.system("python3 LIK.py")
#the end
    




