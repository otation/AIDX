def add():
	print('덧셈 결과 :', num1 + num2)
def sub():
	print('뺄셈 결과 :', num1 -  num2)
def mul():
	print('곱셈 결과 :', num1 * num2)
def div():
	print('나눗셈 결과 :', num1 / num2)

while True:
	num1 = float(input('첫 번째 숫자 입력 :'))

	num2 = float(input('두 번째 숫자 입력 :'))

	selectOperator = int(input('연산자 선택, 1. +, 2. -, 3. *, 4. / 5. exit'))

	if(selectOperator == 1):
		add()
	elif(selectOperator == 2):
		sub()
	elif(selectOperator == 3):
		mul()
	elif(selectOperator == 4):
		div()
	else:
		break
