number = int(input("정수 입력:"))

if number > 0:
	if number%2 == 0:
		print("짝수입니다.")
	else:
		print("홀수입니다.")
else:
	print("0이나 음의 정수입니다.")
