
dan = int(input("단을 입력하세요.:"))

while True:
	if dan ==0:
		break

	for i in range(9):
		for j in range(9):
			print("{} * {} = {}".format(dan, j+1, (dan*(j+1))))
	print()
	dan = int(input("단을 입력하세요.:"))
