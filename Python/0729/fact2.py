n = int(input("양의 정수 입력 :"))

fact= 1

print("{}! = ".format(n), end='')

for i in range(n, 0,-1):

	if i != 1:
		print("{} X ".format(i), end='')
	else:
		print("{} = ".format(i), end='')

	fact *= i

print(fact)
