#! /usr/bin/python
import os
import sys
import time
wait = time.sleep
from Settings.temp import color

def windowslogo():
	os.system('cls')
	print(color.blue+'███████████████████████████████████████████████████​​​​​')
	print('█▄─▄─▀█▄─▄███▄─██─▄█▄─▄▄─█▀▀▀▀▀██▄─▄▄─█▄─█─▄█▄─▄▄─█​​​​​')
	print('██─▄─▀██─██▀██─██─███─▄█▀█████████─▄█▀██▄─▄███─▄█▀█​​​​​')
	print('▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀​​​​​'+color.nocolor)
	try:
		from Settings.Config import Animation
	except Exception:
		print(color.red+'Application Crashed! , Please Restart!'+color.nocolor)
		exit()
	if Animation==True:
		words = color.yellow+'                Wₑlcₒmₑ Tₒ Blᵤₑ₋ₑyₑ                '+color.nocolor
		for char in words:
			wait(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()
		print('')
		words = color.yellow+'         Follow Me On Instagram @adel_naim         '+color.nocolor
		for char in words:
			wait(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()
		print('\n')
	else:
		print(color.yellow+'                Wₑlcₒmₑ Tₒ Blᵤₑ₋ₑyₑ                '+color.nocolor)
		print(color.yellow+'         Follow Me On Instagram @adel_naim         '+color.nocolor)
		print('\n')
		
def linuxlogo():
	try:
		from Settings.Config import Animation
	except Exception:
		print(color.red+'Application Crashed! , Please Restart!'+color.nocolor)
		exit()
	os.system('clear')
	os.system('figlet B-Eye | lolcat')
	if Animation==True:
		words = color.yellow+'[Welcome To Blue-Eye]'+color.nocolor
		for char in words:
			wait(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()
		print('')
		words = color.yellow+'[!]Follow Me On Instagram @adel_naim'+color.nocolor
		for char in words:
			wait(0.05)
			sys.stdout.write(char)
			sys.stdout.flush()
		print('\n')
	else:
		print(color.yellow+'[Welcome To Blue-Eye]'+color.nocolor)
		print(color.yellow+'[!]Follow Me On Instagram @adel_naim'+color.nocolor)
		print('\n')
		
