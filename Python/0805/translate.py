def introKor():
	print('안녕.')
def introEng():
	print('Hello.')
def introJap():
	print('곤니치와.')

while True:
	selecNum = int(input('Where are you from? 1. 한국, 2.USA, 3.Jap 4.exit :'))

	if(selecNum == 1):
		introKor()
	elif(selecNum == 2):
		introEng()
	elif(selecNum == 3):
		introJap()
	else: 
		break

