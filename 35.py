import webbrowser
from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
from random import randint
from datetime import datetime
import random
import os
import ssl
from urllib.parse import quote
from secrets import compare_digest
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *

class colors:
    cyan = '\033[36m'
    pink = '\033[95m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

now = datetime.now()

text1 = "\033[1;32m ↷✦; w e l c o m e > Tool By:\033[1;35m Hồ Xuân Phú"
text2 = " ═══════════════════════════════════════════════════════════"
text3 = "\033[1;36mFix Tool :\033[1;35m Hồ Xuân Phú"
text4 = " ═══════════════════════════════════════════════════════════"
text5 = "\033[1;33mHot Treo"

text20 ="\033[93m⋘ 𝑙𝑜𝑎𝑑𝑖𝑛𝑔 𝑑𝑎𝑡𝑎... ⋙"

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
sleep(0)
print(text1)
sleep(0)
print(text2)
sleep(0)
print(text3)
sleep(0)
print(text4)
sleep(0)
print(text5)
sleep(0)

print("--------------------------------")
sleep(1/6)
###########################
print("**Link_Channel nào không spam thì để trống")
print("Channel_id nào không spam thì để là 0")
sleep(1/6)
###########################
print("--------------------------------")
print("   NHẬP THÔNG TIN TÀI KHOẢN  ")
print(".Vui lòng làm đúng các bước")
print(".Nếu sai bước nào xin hãy làm lại từ đầu")
# webbrowser.open("")
sleep(1/6)
print("")
au = input("Nhập authorization(Token) : ")
file_list = []
data_list = []
print("")
print("--------------------------------")

r1 = input(f'Nhập Link mời Channel thứ 1 (VD:https://discord.gg/tB..2..N) : ')
ci1 = int(input(f'Nhập Channel_id 1: '))
print("")
print("--------------------------------")
r2 = input(f'Nhập Link mời Channel thứ 2 (Để trống nếu không spam) : ')
ci2 = int(input("Nhập Channel_id 2 ( điền 0 nếu kh cần ): "))
print("")
print("--------------------------------")
r3 = input(f'Nhập Link mời Channel thứ 3 (Để trống nếu không spam) : ')
ci3 = int(input(f'Nhập Channel_id 3 ( điền 0 nếu kh cần ): '))
sleep(0.6)
###########################
print("")
duy1=input(f'Nhập nội dung muốn spam : ') 
file_list.append(duy1)
sleep(0.6)
###########################
print("")
cd = int(input("Nhập thời gian delay(1 = 1s) : "))
sleep(1)
###########################
print("---------------------------")
sleep(0.4)
print("🌸Sử Dụng Tool Vui Vẻ Nha😇")
sleep(1/6)
# clear the screen

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
sleep(1)
print(text20)
sleep(1/6)
###########################
header_data = {
    "content-type": "application/json",
    "user-agent": "discordapp.com",
    "authorization": (au),
    "host": "discordapp.com",
    "referer": (r1),
    "referer": (r2),
    "referer": (r3),
}

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def get_connection():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message_data):
    try:
        # option v...
        conn.request(
            "POST", f"/api/v9/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("     dvm w hduy     ")
            pass
        else:
            stderr.write(f"HTTP received {resp.status}: {resp.reason}\n")
            pass
    except:
        stderr.write("Lỗi, Hãy Kiểm Tra Lại\n")

def main():
    message_data = {
        "content": (duy1),    
        "tts": "false",
    }
    send_message(get_connection(), (ci1),
                 dumps(message_data))  # option channel_id
    send_message(get_connection(), (ci2),
                 dumps(message_data))  # option channel_id
    send_message(get_connection(), (ci3),
                 dumps(message_data))  # option channel_id

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        sleep(1)
        time_sec -= 1
    print(" >> ")

if __name__ == '__main__':
    while True:
        print("--------------------------")
        main()
        print("--------------------------")
        countdown(cd)