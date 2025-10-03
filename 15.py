import requests,os,sys,threading
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
red='\u001b[31;1m'
yellow='\u001b[33;1m'
xanhlam='\u001b[32;1m'
def clear():
    if os.name=='nt':os.system('cls')
    else:os.system('clear')
def check(email):
    headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'NGUserID=yj1tIbPS-755-1679664183-0; wa=3f6ff98bc0e953b2a3240e4909cf1c2e; ua_id=e0c2e186-5a59-4f48-a233-7aeda508b6d2; GDNA=true; uiconsent={%22permissionFeature%22:[%22fullConsent%22]}; _gid=GA1.2.855640965.1681254686; __gads=ID=4dc4b020bc6a31b6:T=1681254688:S=ALNI_Mb1u-NVS8LBSMBvw3_yl5T9Pgt2-Q; __gpi=UID=00000bf2b55215f0:T=1681254688:RT=1681254688:S=ALNI_MZc3NziPvAtsj4kIpYR0yoglNgh2Q; _autuserid2=7214546460232972442; cto_bidid=WJ2jRl9uc2NtWlFwRmppeG9QM3RGbFl3MFQ1NTNVQkNGQmhjZVcwOWRjR2NkMDUlMkJpNFYxOXN6Q3hyYkNzalVRRWlpeDRlZThPOG1zeFZ3UTc5Z0R6MzJNWVZPTnVvZmJCdUVaVWVpc1YxTkZJenZvJTNE; cookieKID=kid@autoref@www.mail.com; AB_COOKIE=A; cookieKID=kid%40autoref%40signup.mail.com; cookiePartner=kid%40autoref%40signup.mail.com; cto_bundle=OA2gc19LVTAwOXlFQklKZ3dCMElBRHhRMTBMNSUyRkZTeWJhM2xYciUyQmZ3RjhSUzk3NGVSQ2tqRFhsRjNsWHVIYlZXUUdhSmlRRWZGeXFGcUp0JTJCazRQQlpScVglMkZRd2FySHh4MTZtSHdEcG4wbWZYOXZjSVJvZUE4MWVGR3RXakRVQTdlWVFXJTJGS2hYMUtEUEM5U2V5WkdtYUdOZ0dnJTNEJTNE; _gat_UA-56857562-5=1; TSd783f027027=0850089c4aab2000354020e98822ae6cdf10acca176597d737f73415073f78f38f1e7c8087f0a494088bc5789a1130001eb70b57d98679f30efc81711fd33a0e7c9887ccc567d8c01beaca890e298331a51f188c203c9f8b7f6f7acb8cb1f106; _ga=GA1.1.1264363794.1681254686; _ga_V2FMR8VFB6=GS1.1.1681254685.1.1.1681255025.58.0.0',
                    'Referer': 'https://www.mail.com/',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

    response = requests.get('https://signup.mail.com/', headers=headers).text
    token = response.split('"accessToken": "')[1].split('"')[0]
    ccuid = response.split('"clientCredentialGuid": "')[1].split('"')[0]
    headers = {
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': f'Bearer {token}',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    'Cookie': 'NGUserID=yj1tIbPS-755-1679664183-0; wa=3f6ff98bc0e953b2a3240e4909cf1c2e; ua_id=e0c2e186-5a59-4f48-a233-7aeda508b6d2; GDNA=true; uiconsent={%22permissionFeature%22:[%22fullConsent%22]}; _gid=GA1.2.855640965.1681254686; __gads=ID=4dc4b020bc6a31b6:T=1681254688:S=ALNI_Mb1u-NVS8LBSMBvw3_yl5T9Pgt2-Q; __gpi=UID=00000bf2b55215f0:T=1681254688:RT=1681254688:S=ALNI_MZc3NziPvAtsj4kIpYR0yoglNgh2Q; _autuserid2=7214546460232972442; cto_bidid=WJ2jRl9uc2NtWlFwRmppeG9QM3RGbFl3MFQ1NTNVQkNGQmhjZVcwOWRjR2NkMDUlMkJpNFYxOXN6Q3hyYkNzalVRRWlpeDRlZThPOG1zeFZ3UTc5Z0R6MzJNWVZPTnVvZmJCdUVaVWVpc1YxTkZJenZvJTNE; cookieKID=kid@autoref@www.mail.com; AB_COOKIE=A; cookieKID=kid%40autoref%40signup.mail.com; cookiePartner=kid%40autoref%40signup.mail.com; cto_bundle=OA2gc19LVTAwOXlFQklKZ3dCMElBRHhRMTBMNSUyRkZTeWJhM2xYciUyQmZ3RjhSUzk3NGVSQ2tqRFhsRjNsWHVIYlZXUUdhSmlRRWZGeXFGcUp0JTJCazRQQlpScVglMkZRd2FySHh4MTZtSHdEcG4wbWZYOXZjSVJvZUE4MWVGR3RXakRVQTdlWVFXJTJGS2hYMUtEUEM5U2V5WkdtYUdOZ0dnJTNEJTNE; TSd783f027027=0850089c4aab200000dfe81e3ba08e7fbe59870c197575daba997ce6d4c7c8009f0c8b6ccbc00a34084dd1619f113000a37e3dac48742088e3863713cfb058148765411191ea707ff3d17dacfa8c131678f8db0b28c7355ec87fe894aaacd019; _gat_UA-56857562-5=1; _ga=GA1.1.1264363794.1681254686; _ga_V2FMR8VFB6=GS1.1.1681254685.1.1.1681255222.57.0.0',
                    'Origin': 'https://signup.mail.com',
                    'Referer': 'https://signup.mail.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'X-CCGUID': ccuid,
                    'X-REQUEST-ID': 'a5722cb8-1812-499c-be2d-f90ad245c86f',
                    'X-UI-APP': '@umreg/registration-app2/7.2.5',
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

    json_data = {
                    'emailAddress': email,
                    'firstName': '',
                    'lastName': '',
                    'birthDate': '',
                    'city': '',
                    'countryCode': 'US',
                    'suggestionProducts': [
                        'mailcomFree',
                    ],
                    'maxResultCountPerProduct': '10',
                    'mdhMaxResultCount': '5',
                    'initialRequestedEmailAddress': '',
                    'requestedEmailAddressProduct': 'mailcomFree',
                }

    response = requests.post('https://signup.mail.com/suggest/rest/email-alias/availability',headers=headers,json=json_data,).json()
    try:
        a = response['emailAddressAvailable']
        if a == False:
            print(red+email,"-> Live")
        elif a == True:
            print(xanhlam+email,"-> Die")
            open(luusave,'a+').write(email+'\n')
    except:
        b = response['errors'][0]['status']
        if b == '422':
            print(yellow+email,"-> Lỗi")
        elif b == '401':
            while True:
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'NGUserID=yj1tIbPS-755-1679664183-0; wa=3f6ff98bc0e953b2a3240e4909cf1c2e; ua_id=e0c2e186-5a59-4f48-a233-7aeda508b6d2; GDNA=true; uiconsent={%22permissionFeature%22:[%22fullConsent%22]}; _gid=GA1.2.855640965.1681254686; __gads=ID=4dc4b020bc6a31b6:T=1681254688:S=ALNI_Mb1u-NVS8LBSMBvw3_yl5T9Pgt2-Q; __gpi=UID=00000bf2b55215f0:T=1681254688:RT=1681254688:S=ALNI_MZc3NziPvAtsj4kIpYR0yoglNgh2Q; _autuserid2=7214546460232972442; cto_bidid=WJ2jRl9uc2NtWlFwRmppeG9QM3RGbFl3MFQ1NTNVQkNGQmhjZVcwOWRjR2NkMDUlMkJpNFYxOXN6Q3hyYkNzalVRRWlpeDRlZThPOG1zeFZ3UTc5Z0R6MzJNWVZPTnVvZmJCdUVaVWVpc1YxTkZJenZvJTNE; cookieKID=kid@autoref@www.mail.com; AB_COOKIE=A; cookieKID=kid%40autoref%40signup.mail.com; cookiePartner=kid%40autoref%40signup.mail.com; cto_bundle=OA2gc19LVTAwOXlFQklKZ3dCMElBRHhRMTBMNSUyRkZTeWJhM2xYciUyQmZ3RjhSUzk3NGVSQ2tqRFhsRjNsWHVIYlZXUUdhSmlRRWZGeXFGcUp0JTJCazRQQlpScVglMkZRd2FySHh4MTZtSHdEcG4wbWZYOXZjSVJvZUE4MWVGR3RXakRVQTdlWVFXJTJGS2hYMUtEUEM5U2V5WkdtYUdOZ0dnJTNEJTNE; _gat_UA-56857562-5=1; TSd783f027027=0850089c4aab2000354020e98822ae6cdf10acca176597d737f73415073f78f38f1e7c8087f0a494088bc5789a1130001eb70b57d98679f30efc81711fd33a0e7c9887ccc567d8c01beaca890e298331a51f188c203c9f8b7f6f7acb8cb1f106; _ga=GA1.1.1264363794.1681254686; _ga_V2FMR8VFB6=GS1.1.1681254685.1.1.1681255025.58.0.0',
                    'Referer': 'https://www.mail.com/',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                response = requests.get('https://signup.mail.com/', headers=headers).text
                token = response.split('"accessToken": "')[1].split('"')[0]
                ccuid = response.split('"clientCredentialGuid": "')[1].split('"')[0]
                headers = {
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': f'Bearer {token}',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json',
                    'Cookie': 'NGUserID=yj1tIbPS-755-1679664183-0; wa=3f6ff98bc0e953b2a3240e4909cf1c2e; ua_id=e0c2e186-5a59-4f48-a233-7aeda508b6d2; GDNA=true; uiconsent={%22permissionFeature%22:[%22fullConsent%22]}; _gid=GA1.2.855640965.1681254686; __gads=ID=4dc4b020bc6a31b6:T=1681254688:S=ALNI_Mb1u-NVS8LBSMBvw3_yl5T9Pgt2-Q; __gpi=UID=00000bf2b55215f0:T=1681254688:RT=1681254688:S=ALNI_MZc3NziPvAtsj4kIpYR0yoglNgh2Q; _autuserid2=7214546460232972442; cto_bidid=WJ2jRl9uc2NtWlFwRmppeG9QM3RGbFl3MFQ1NTNVQkNGQmhjZVcwOWRjR2NkMDUlMkJpNFYxOXN6Q3hyYkNzalVRRWlpeDRlZThPOG1zeFZ3UTc5Z0R6MzJNWVZPTnVvZmJCdUVaVWVpc1YxTkZJenZvJTNE; cookieKID=kid@autoref@www.mail.com; AB_COOKIE=A; cookieKID=kid%40autoref%40signup.mail.com; cookiePartner=kid%40autoref%40signup.mail.com; cto_bundle=OA2gc19LVTAwOXlFQklKZ3dCMElBRHhRMTBMNSUyRkZTeWJhM2xYciUyQmZ3RjhSUzk3NGVSQ2tqRFhsRjNsWHVIYlZXUUdhSmlRRWZGeXFGcUp0JTJCazRQQlpScVglMkZRd2FySHh4MTZtSHdEcG4wbWZYOXZjSVJvZUE4MWVGR3RXakRVQTdlWVFXJTJGS2hYMUtEUEM5U2V5WkdtYUdOZ0dnJTNEJTNE; TSd783f027027=0850089c4aab200000dfe81e3ba08e7fbe59870c197575daba997ce6d4c7c8009f0c8b6ccbc00a34084dd1619f113000a37e3dac48742088e3863713cfb058148765411191ea707ff3d17dacfa8c131678f8db0b28c7355ec87fe894aaacd019; _gat_UA-56857562-5=1; _ga=GA1.1.1264363794.1681254686; _ga_V2FMR8VFB6=GS1.1.1681254685.1.1.1681255222.57.0.0',
                    'Origin': 'https://signup.mail.com',
                    'Referer': 'https://signup.mail.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'X-CCGUID': ccuid,
                    'X-REQUEST-ID': 'a5722cb8-1812-499c-be2d-f90ad245c86f',
                    'X-UI-APP': '@umreg/registration-app2/7.2.5',
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                json_data = {
                    'emailAddress': email,
                    'firstName': '',
                    'lastName': '',
                    'birthDate': '',
                    'city': '',
                    'countryCode': 'US',
                    'suggestionProducts': [
                        'mailcomFree',
                    ],
                    'maxResultCountPerProduct': '10',
                    'mdhMaxResultCount': '5',
                    'initialRequestedEmailAddress': '',
                    'requestedEmailAddressProduct': 'mailcomFree',
                }

                response = requests.post('https://signup.mail.com/suggest/rest/email-alias/availability',headers=headers,json=json_data,).json()
                try:
                    a = response['emailAddressAvailable']
                    if a == False:
                        print(red+email,"-> Live")
                        break
                    elif a == True:
                        print(xanhlam+email,"-> Die")
                        open(luusave,'a+').write(email+'\n')
                        break
                except:
                    b = response['errors'][0]['status']
                    if b == '422':
                        print(yellow+email,"-> Lỗi")
                        break
                    elif b == '401':
                        continue
def do_long(thread_step):
    try:
        for i in range(thread_step,len(file),luong):
            check(file[i])
    except:
	    pass
clear()
while True:
    try:
        name = input(Colorate.Diagonal(Colors.green_to_white, f"File Mail: "))
        open(name,"r",encoding = 'latin-1').read()
        break
    except:
        print(f"{red}No File !")
        continue
luusave = input(Colorate.Diagonal(Colors.green_to_white, f"Save Mail Die: "))
luong = int(input(Colorate.Diagonal(Colors.green_to_white, f"Theadring: ")))
clear()
mo_mail = open(name,encoding='latin-1')
file = mo_mail.read().split("\n")
threads = []
for i in range(luong):
    threads += [threading.Thread(target = do_long,args=(i,))]
for i in range(luong):
    threads[i].start()
for i in range(luong):
    threads[i].join()
clear()


quit()