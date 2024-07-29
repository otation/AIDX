import random

x = random.randint(1,100)
y = random.randint(1,100)

if x >= y:
	a = x
	b = y
else:
	a = y
	b = x

ran = random.randint(0,3)

if ran == 0:
	answer = int(input(f"{a} + {b} = "))
	flag = (answer == (a+b))

elif ran == 1:
	answer = int(input(f"{a} * {b} = "))
	flag = (answer == (a*b))

elif ran == 2:
	answer = int(input(f"{a} / {b} = "))
	flag = (answer == ,0(a/b))
else:
	answer = int(input(f"{a} - {b} = "))
	flag = (answer == (a-b))

print(flag)
