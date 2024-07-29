loopCnt = int(input("층의 개수를 입력하세요."))

for n1 in range(loopCnt):
	for n2 in range(loopCnt-n1-1):
		print(' ', end='')
	for n3 in range((n1+1)-1):
		print(' ', end='')
	for n3 in range((n1+1)-1):
		print('*', end='')

	print()
