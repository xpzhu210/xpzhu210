import os,sys,requests
from time import sleep
htool=f"[🌸] ==> "
list_id_name_page=[]
__TOOL__='Tool Get Cookie Page Thường & Page Pro5'
__AUTHOUR__='HỒ XUÂN PHÚ'
__TIKTOK__=' @XPZHU210'
__YOUTUBE__='HỒ XUÂN PHÚ'
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.00)
   print()
def banner():
    banner=f"""
\033[1;31m  ██╗░░██╗░█████╗░  ██╗░░██╗██╗░░░██╗░█████╗░███╗░░██╗  ██████╗░██╗░░██╗██╗░░░██╗
  \033[1;34m██║░░██║██╔══██╗  ╚██╗██╔╝██║░░░██║██╔══██╗████╗░██║  ██╔══██╗██║░░██║██║░░░██║
  \033[1;33m███████║██║░░██║  ░╚███╔╝░██║░░░██║███████║██╔██╗██║  ██████╔╝███████║██║░░░██║
  \033[1;32m██╔══██║██║░░██║  ░██╔██╗░██║░░░██║██╔══██║██║╚████║  ██╔═══╝░██╔══██║██║░░░██║
  \033[1;35m██║░░██║╚█████╔╝  ██╔╝╚██╗╚██████╔╝██║░░██║██║░╚███║  ██║░░░░░██║░░██║╚██████╔╝
  \033[1;36m╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
    echo(banner)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def thanh():
    echo(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
clear()
banner()
cookie=input(f'{htool}Vui Lòng Nhập Cookie Facebook Chứa Page: ')
headers_check_live={
    'authority':'mbasic.facebook.com',
    'cache-control':'max-age=0',
    'sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'upgrade-insecure-requests':'1',
    'origin':'https://mbasic.facebook.com',
    'content-type':'application/x-www-form-urlencoded',
    'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site':'same-origin',
    'sec-fetch-mode':'navigate',
    'sec-fetch-user':'?1',
    'sec-fetch-dest':'document',
    'referer':'https://mbasic.facebook.com/',
    'accept-language':'en-US,en;q=0.9',
    'cookie':cookie
}
try:
    find_data=requests.get('https://mbasic.facebook.com/',headers=headers_check_live).text
    fb_dtsg=find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest=find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    thanh()
    exit(f'Vui Lòng Kiểm Tra Lại Cookie !!!')
headers_getid={
    'cookie':cookie,
}
data={
    'fb_dtsg':fb_dtsg,
    'jazoest':jazoest,
    'variables':'{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id':'5300338636681652'
}
get_id_page=requests.post(f'https://www.facebook.com/api/graphql/',headers=headers_getid,data=data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
for i in get_id_page:
    uid_page=i['profile']['id']
    name_page=i['profile']['name']
    gomlist=f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
clear()
banner()
print(f'{htool}Tìm Thấy '+str(len(list_id_name_page))+' Page Thường & Page Pro5')
thanh()
lua_chon=input(f'{htool}Lưu Cookie Kèm Tên Page & Uid Page [y/n]: ')
thanh()
if lua_chon=='y':
    file=input(f'{htool}Vui Lòng Nhập File Lưu Cookie: ')
    for a in get_id_page:
        uid_page=a['profile']['id']
        name_page=a['profile']['name']
        with open(file,'a',encoding='utf-8')as f:
            f.write(f"{cookie};i_user={uid_page}|{name_page}|{uid_page}\n")
else:
    file=input(f'{htool}Vui Lòng Nhập File Lưu Cookie: ')
    for a in get_id_page:
        uid_page=a['profile']['id']
    with open(file,'a',encoding='utf-8')as f:
        f.write(f"{cookie};i_user={uid_page}\n")
thanh()
echo(f'{htool}Đã Lưu Cookie, Vui Lòng Kiểm Tra File')
sleep(1.5)