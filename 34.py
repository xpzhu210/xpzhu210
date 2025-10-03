from urllib.parse import quote
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
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "🌸"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ {trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ {trang}[\033[1;33m•{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ {trang}[\033[1;35m••{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ {trang}[\033[1;32m•••{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ {trang}[\033[1;38m••••{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{vang}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{xanhnhat}REVIEWTOOL247{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = f"""
\033[1;31m  ██╗░░██╗░█████╗░  ██╗░░██╗██╗░░░██╗░█████╗░███╗░░██╗  ██████╗░██╗░░██╗██╗░░░██╗
  \033[1;34m██║░░██║██╔══██╗  ╚██╗██╔╝██║░░░██║██╔══██╗████╗░██║  ██╔══██╗██║░░██║██║░░░██║
  \033[1;33m███████║██║░░██║  ░╚███╔╝░██║░░░██║███████║██╔██╗██║  ██████╔╝███████║██║░░░██║
  \033[1;32m██╔══██║██║░░██║  ░██╔██╗░██║░░░██║██╔══██║██║╚████║  ██╔═══╝░██╔══██║██║░░░██║
  \033[1;35m██║░░██║╚█████╔╝  ██╔╝╚██╗╚██████╔╝██║░░██║██║░╚███║  ██║░░░░░██║░░██║╚██████╔╝
  \033[1;36m╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░

\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
clear()
runbanner(chontool)
idcanspam=input(f'\033[1;97m[\033[1;31m🌸\033[1;97m] {xanhnhat}id box:{vang} ')
while True:
      ck=input(f'\033[1;97m[\033[1;31m🌸\033[1;97m] {xanhnhat}Nhập cookie:{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')   
        runbanner(chontool)
params = {
      "icm": '1',
    }
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"87",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }
SO_CHUI = [
f"mày cầm 3 cái ngôn copy của mày gõ với anh hả bị anh đạp vô cái họng dái mày ở bên bờ đường a cầm súng tỉa búng vô cái lỗ họng thối m ẹ mày ngoài lề đường cn đ/ĩ m ẹ mày óc cac~~ bị anh bem dồn 1 góc cạnh của cái bướm m ẹ mày thâm như dái lợn sắp nghẻo nhà tao mà con đ/ĩ ngu ăn boài sống qua ngày giúp tăng thêm trình độ ăn hại của mày ~~~ ",
f"đừng bực bội chứ con nít con noi về học đi đừng đú đởn ớt đỏ chứng tỏ em đang cay đừng nói những lời em đang gặp phải chứ  không có ăn học rồi nên nói chuyện bị ngáo hay do m ẹ mày bại liệt não nên sinh ra thằng con bị khờ ngu học phát ngôn những câu bị xã hội xa lánh ruồng bỏ tẩy chay con gái m ẹ mày lết ngoài đường bú phân bò để tránh đói qua ngày ",
f"mày bị óc cứt hay sao z hả mà t nói m dell hiểu hay bố phải nhét cứt vào đầu m thì m mới thông hả con óc Lon ơi lêu lêu thằng ngu không làm gì được cay anh kìa ơ hay óc chó ơi m sủa mạnh mẽ lên sao lại bị dập rồi oc chó ko trình lên đây sủa mạnh mẽ lên anh chơi mày cả ngày mà ơ hay óc chó ơi m sủa mạnh mẽ lên sao lại bị dập rồi Một lũ xam cu lên đây đú ửa ngôn thì nhạt như cái nước Lon của con đỉ m ẹ cm v hăng lên đi con m ẹ mày bị t xé rách mu sao chối ",
f"tao có noti cn boài con Lon sợ tao:))) tí bố cap úp tbg:)) hình ảnh cn bẻm con Lon bị chà đạp:)) úi cái cn giẻ rách:))) ccho làm mẫu sủa cha mày coi tí đi con Lon thằng nghịch tử sao m giết cha m thế cn Lon m nỡ đút con c/ac vào cái Lon hết tinh dịch của má m vậy con Lon ",
f"con đ/ĩ m ẹ mày bị tao cầm đinh ba xiên chết tại chỗ thằng bố mày ôm hận tao qua báo thù cho con m ẹ nó còn không xong bị tao cầm phóng lợn xiên qua đầu của bố mày máu rơi như tinh trùng bố của mày bắn vào lỗ Lon m ẹ mày ",
f"cn đỉ chó vô danh bị tao gõ dồn mày ra một góc cn đú war hoảng loạn đi cầu cứu thằng bố mày thương con qua hỏi tội tao bị tao phóng xe đâm chết cả nhà mày đầu rơi lả tả như cách thằng bố mày ném viên gạch vào đầu m ẹ mày ",
f"mày gõ ba cái ngữ từ tám phương tám hướng đem lên đây ra thế hào hùng tao tướng đầu sở trăm ngàn trận thâng ai mà ngờ đâu ba cái đồng ngôn từ thời tống mang lên đây định làm trò hài cho thiên hạ nó cười rầm rộ hay là con đi m ẹ mày múa kiếm trước cổng chợ để mà mưu sinh kiếm sống ",
f"sợ quá sợ quá cái loz hồng dở giọng show ngôn quèn hay gì ))= kể cả cái quần rách đôi của mấy con phò phèn trúa múa máy trong bar club cũng đéo phèn bằng cái ngôn cóp mạng rồi lôi ra tap người khác như ai đó đâu ha. hay lại cần anh mày nhét vô đầy họng mày con c/ac của anh thì m mới chịu câm mõm chó của m lại à? Ngôn thì không thấy toàn thấy giở ra là nói người ta tung ngôn tung war các thứ, nói thật chứ ngôn đéo gì toàn sài đi sài lại cố để chống cự cho bớt nhục cái mã tướng, cái bản chất ngông ngông của mấy bọn trẩu mới mọc lông mu chứ oai oai cái đếc gì, m ẹ hài ỉa vãi lờ kaka ngôn tap cùi thế thì có mấy em mầm non mới sợ nên cứ tap bao giờ không tap được thì đội m ẹ cái đầu b lên cho bớt nhục nha loz hồng óc chó nghịch tử sát hại cha đẻ bị tao gõ dồn cho die con m ẹ mày luôn chứ ở đó mà đú với tao hả thằng chó đẻ ăn cứt của mình bị tao bắt gặp mày xấu hổ quá nên nhảy lầu tự tử ba m ẹ mày thấy vậy tự tử theo thằng con óc chó ",
f"container nó mất lái nó lại ùi vào cái Lon con đ/ĩ m ẹ mày đó con nghiệt súc. Đã ngu thì câm m ẹ mõm Lon lại cho người ta thương chứ đừng có xàm c/ac nừa nạt nừa mỡ cho người ta ghét, lời mày thốt ra hãm Lon đến mức gây tổn hại cho bầu không khí này nên không nói được gì tốt đẹp thì thôi dẹp con m ẹ mày đi, sống đéo từ tế thì tử vong m ẹ đi cho đỡ chật đất. Nói ít nhưng hiểu nhiều chứ giống loài máu Lon nhiều hơn máu não như mày thì nói nhiều cũng chả hiểu được bao nhiêu đâu con đồn lì a thật kinh tởm cho cho những con người xung quanh mày, được bú buổi trai nên ra dáng con phò trước mặt mọi người, gái đã nứng rồi thì banh Lon ra tao gạ cho mười anh địt nát Lon mày nha con đ/ĩ của thế giới, mày bị thiếu ăn hà suốt ngày húp tinh trùng vậy con phò quốc dân?trong bầu không khí ô nhiễm của mày tạo ra đã làm trái đất sắp bị ô nhiễm mức nghiêm trọng nên tao sẽ chặt xác mày ra thành từng mành rồi đầu mày tao sẽ cho chó gặm đến lòi hai con mắt Lon của mày ra còn Lon mày thì tao sẽ đá bay ra khỏi vũ trụ này rồi đá văng cái nếp ngông c/ac của mày ra khỏi thế giới này păi con uống dâm thủy thay cơm nha con Lon mãi mãi liếm chân dòng họ nhà tao ",
f"con gái m ẹ mày bị tao chịch bắn tinh như khẩu 6 nòng vào lỗ Lon m ẹ mày đến nỗi toạc bướm con gái m ẹ mày phải tắc đái nên đái bằng mồm bị xã hội kì thị xa lánh con gái m ẹ mày tự ái nên thắt cổ tự tử cha m ẹ mày thấy thương xót cho nó không muốn để cn gái m ẹ nó  mình dưới địa ngục nên nhảy lầu tự tử rơi xuống đất nát bét lên đầu còn bị đàn chim ỉa lên xác của cha m ẹ mày ",
f"mày là thằng con bất hiếu sát hại cha m ẹ đẻ của mày bị tao bắt được tung lên web của những thằng nghịch tử bị chúng nó ghét quá tìm nhà mày đánh mày như chó khiến mày liệt c/ac đéo đái được phải đái bằng mồm họ hàng ruồng bỏ mày không nhận nuôi mày vì mày đái bằng mồm mày hối hận khi sát hại cha m ẹ mày nên nhảy lầu tự tử đầu đập vào tường văng ra bãi cứt chó mới vừa rơi từ đít chó xuống đất 🤣🤣 :)) ",
f"Bộ lúc ông trời thả não mày cầm ô che à hay máu kinh tràn lên hoà cùng với máu não mày vậy? Trời ơi nhìn cái não mày kia, sao mà nó có thể trơn tru, láng mịn, không một vết nhăn thế nhỉ? Đại não và tất cả các thành phần trong não mày không phát triển à? Bằng tất cả sự văn minh thành thật mong mày thả lòng cơ nhai, khép hai hàm lại vì phát ngôn của mày gây ảnh hưởng thiếu tích cực đến chất lượng không khí lắm! Thật thú vị tạo nên báo cáo cho tổ chức y khoa thế giới của một trường hợp thai nhi được sinh ra với bộ não rất ở trong bụng m ẹ ví dụ điển hình đó là mày đó thứ ôn Lon não phẳng ạ.Lưu ý: đừng cố văn minh vì một con đ/ĩ ngu Lon như mày không thể hiểu nổi đâu ",
f"t kể mày nghe nè con người yêu m ý t chịch nó lúc đầu t hôn đá lưỡi nó rồi t xé quần áo nó ra t xoa bú vú rồi qua t liếm móc Lon ngiu m đó t lúc đầu cọ vô Lon ny mày rồi dần dần tao đút vào kịch liệt con ny m rên la thảm thiết trong vô vọng ",
f"ngu chưa kìa thg phế vật bị oto cán nát đầu mày mùi hôi nồng nặc như cách tao bắn tinh dịch vào lỗ âm đạo m ẹ mày đến tràn ra như mưa lũ sóng thần m ẹ mày phải liếm sạch để đc sống "
f"có trình để có được sự ủng hữu sơn tĩnh lại gọi cho anh lm nháy nút lưỡi vs nó không thể thay đổi nội m hả bác năm mới giáp đi học đi tin t có một cái tên được chú trọng đến việc của bạn thân mến mà không cần thiết của m bên trong nhóm nó khó khăn cho t coi là kẻ bám vào thành phố Hồ Chí làm j z tr ng coi trọng công nghiệp hoá đuma ảnn mạng lưới phân ",
f"gõ mà tưởng đâu mày đi cóp sớ từ đẩu đâu về đem qua đây trình bày lên còn tụi anh đây câu nào câu đó đều tăm tắp còn làm lại mày luôn á phải đi cầu cứu mấy con ba gai qua lại đây gõ chung không hồi tử nạn ta nói ha con đ/ĩ m ẹ mày cây khô thì tô màu lá chứ đâu có cái tá điền hèn hạ như con đ/ĩ m ẹ mày sáng bốc chọp cứt non ngồi ăn như ch ết đói cái thời 1945 giặc qua xâm lượt mà rượt đuổi con đ/ĩ m ẹ mày lên tới ngay cái đường cao tốc mà cái tính bốc đồng xạo Lon xe hơi 4 bánh nó c án ngang cái chân phải gãy làm đôi đâu con mọi rợ nó gõ sớ diễn loạn lên mà cái ngữ thì như đ ấm vô Lon bà già nó trước khi qua đời không dị á nói không sai con bất hiếu ",
f"con đồng tính luyến ái sang đen con bóng lẹo cái để cái tên bé ba mà có cây đinh ba ở dưới háng đéo biết mắc cỡ lên đây kiếm chuyện thị thi để cho anh mày nổi trận lôi đình m lôi đầu con đ ỉ m ẹ mày ra xét xử mà đứng trước cái vành móng ngựa mà tay chân run lẩy bẩy không nói nên lời mà cúi đầu cắm cổ thành khẩn khai báo từng cái tội trạng ra trước mặt công chúng rồi nghe toà tuyên án nhận được cái bản án tư? hình rồi hai dòng lệ rơi trên gò má nhìn mặt không khác gì con cá thác lác luôn ",
f"nhìn người ta gõ mà không một miếng run sợ nôn ra câu nào là dồn dập sát thương lên cơ thể con người mày câu đó chứ ai như mặt 🐶 mày lấp ló dưới cống hửi mùi rac' như mấy con chớp nhát không dám bậc lại ai đó cái loại ba gai như mày người ta chưa chia năm sẻ bảy lên hên cho cái cuộc sống lâm đi bia đát của gia môn mày dữ lắm rồi đó chắc con gái m ẹk mày đẻ mà không xem ngày xem tháng nên oan gia nghiệp chướng đẻ ra cái con nqu văn dốt lý như mày đó con đi~ lòn nghĩ sao người ta gõ ra câu nào cũng thấm đậm mùi mau' trên cở thể ma' mày còn mày gõ thì như nước đổ lá môn nước xối đầu vịt ",
f"tao gõ vừa nhanh vừa lẹ mà còn không sai chính tả còn nhìn lại cái sớ mày gõ sai lên sai xuống như cái bọn nghèo nàn không được học tới nơi tới chốn nên bây giờ gặp người học cao hiểu rộng nên mày kính trọng ba phần còn bảy phần kia là nể phục vì iq người ta quá cao còn mày thì quá thấp cái loại bập bẹ đú war rồi ảo trình có khác gì mấy cn bần cùng sinh đạo tặc không hả bị tao vả cho mấy cái là ngớ người ra mà tưởng bở hả con đ/ĩ điên ",
f"cái ngữ nó loạn xạ hơn cả cảnh cha dượng nó hiếp ch ết con má nó nữa không á mà cứ gắng gượng gõ cho tan tàn bàn phím mày đi ha hồi cái phím bắn lên mắt chảy toe toét máu ra không làm lại còn ôm hận cay đắng ngậm trong miệng mà cứ nhả ra mấy câu từ phải trái bị tụi anh đ á cho lật cái quai hàm ngược lại nói chuyện ấm ớ hay sao vậy đó con cờ hó dở dở ương ương ",
f"thg ngu bị a chọc cho cay điên chạy về mách m ẹ đang chạy bị oto đâm vào lỗ l/o/n m ẹ nó die tại chỗ phân hủy thành đống cut ngoài ruộng làm phân bón cho nhà t bón cho cây tươi tốt bố nó bị t đấm vao xê u đến liệt dương vật như que tăm của bố nó cay không làm gì được tao nên nhờ tao treo cổ cả nhà nó 😑😑 ",
f"bede cay tui kìa chọc tý lên cơn dại nó cbi cắn vô đíc m ẹ nó trong bụi rậm đầy những thằng châu phi hấp diêm m ẹ nó trên cây cổ thụ rơi vào nhà nó nát bét thành vô gia cư không có nhà để ở bốc sít để mưu sinh tích từng đồng bạc lẻ để mua căn nhà rách nát cho nhà nó ở với con cún hay ỉa bậy vào đầu m ẹ nó kìa trời ơi 😆😆 ",
f"cop con đ/ĩ m ẹ mày chui từ ngục tù ra mà không còn tí sức lực bám trụ trong khung hình xử tử anh đưa ra má em cjss vào khóc . ong anh buông lời tha mạng em không biết lượng sức chuốc họa vào thân con đũ m ẹ mày chui từ đống đổ nát hoang tàn ra mà sinh sôi nảy mần nay đẻ đứa  nghiệt súc náo loạn triều cương tao thi hành án tử đưa màu cùng con m ẹ mày ra vành móng ngựaánh sáng chiếu vài mà bả năn nỉ ỉ oi khóc không thành tiếng ",
f"Đụ m ẹ mày chiến tranh điện biên phủ 19 ngày không ngủ là 19 ngày đau khổ của má mày khi bị giặc ngoại xâm đụ liên tục 19 ngày lun á ? Cho ăn tô cháo giữ mạng sống để phục vụ cho lũ ngụy típ má còn m ẹ mày chạy tới miên ms phát hiện bị rơi con giữa chừng khóc thảm thiết ôm hận từng ngày từng ngày bị tức ngực nôn ra máu chết não ngay miên tụi nó đóng gói lại gửi cha mày trên chiến hào thấy thế ổng rủ đồng đội hiếp dâm xác con m ẹ mày rôid đem trôn dưới 3 tấc đấc cùng mày lun ",
f"Trình tao cao như tháp ép phen còn trìng mày như cái đống rác thải ven đường mà xaoh lol mọt cái là củ khoai từ trên trời rơi xuốngcais bịch chúng ngay đầu thằng già mày là cả hai nằm ngoặcngoaif đường thiếu điều muốn cấp thương băng bó mà chưa băng được tới cái phần đầu còn lại đã bị cho người dứoi địa phủ bắt kéo mfy vô tù nằm toeng cái đuoenfg hầm số 9 mà đỉ m ẹ mày xaoh Lon là ăn con cặ cha màymaays hồi chứ ở đó mà bịa gới tao hả ccho đẻ 🤭",
f"lôi con đ/ĩ m ẹ mày đày đọa dưới thân cay mục nát đâm chòi nảy mầm ngấm vào xương tủy má mày uất hận tạ tội tao đi hạ thiển thần tiên còn tha ma gj cưu mang cho co  đ/ĩ m ẹ mày sống qua ngày chứ ất ưỡng lưỡng lự cái câu ca dao thấm nhuần dòng máu của bả tràn lan khắp chốn sạch cái thân thể mày toàn mùi máu tươi phụ mẫu mày tiết ra toàn thân em tê cứng bước đôi chân dẫm đạp lên bia môn thằng cha mày mật tội đi chứ ai thương hại số kiếp súc sinh ô uế như mày nữa ",
f"Cầm cái bản sớ ngon từ thời thằng cha con đ/ĩ meh mày về mà dắt đầu chăn cỏ cho thằngđ/ĩ ms àmy thêm cái nỏii lòng tâm can coi thử ổng có cầm cái điếu cày điếu đổ ổng phang vo đầu mày cái bốp hôn con đỉ má thf lang thang ngoauf đường kiềm tiền mưu sinh co mặt lol mày ở đây kiếm chiện một hồi là tao báo chánh quyền xuông tống cố thằng cha con đ/ĩ meh mày liền nè thằng bê đê xe cán 🖕🏻 ",
f"anh gõ câu nào thấm câu đó mấy óc nhìn mà ao ước chứ như lũ đú lên mấy cái sớ quèn phèn của cái ổ rác nhà mày bị tao dồn vô vực thẳm đạp mày xuống vực toàn cứt rơi vào đầu con gái m ẹ mày ăn hết tránh đói sống qua ngày tao nhìn thấy tao cầm đinh ba thọc vô lỗ l/ồ/n m ẹ mày nên bờ suối bị hiepdam tập thể với 100 anh tây tập gym đạp chết con đ/ĩ m ẹ mày bên bờ biển nát bét bị chó cắn vô đầu dái cha mày đến liệt dương tắc đái m ẹ mày thiếu dục vọng nên thác loạn với ông hàng xóm sida bede đẻ ra mày theo gen ông hàng xóm nên mày bede theo á trời 😑🌶️ ",
]
clear()
runbanner(chontool)
delay=int(input(f'\033[1;97m[\033[1;31m🌸\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 1s) :{vang} '))
while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in SO_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                NOIDUNG = f"\033[1;97m: {nd} \033[1;31m| \033[1;35mThành Công"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}Lỗi bị ngắt kết lối vui lòng kết lối lại mạng để tiếp tục sớ")
          time.sleep(5)
else:
    print(f"{do} sai rồi em ei")   