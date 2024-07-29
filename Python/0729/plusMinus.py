import random

x = random.randint(1,100)
y = random.randint(1,100)

op = random.randint(1,2)

if op == 1:
	answer = int(input(f"{x} + {y} ="))
	flag = (answer == (x+y))
	print(flag)

else:
	if x > y:
		answer = int(input(f"{x} - {y} ="))
		flag = (answer ==(x-y))
		print(flag)
	else:
		answer = int(input(f"{x} + {y} ="))
		flag = (answer ==(x+y))
		print(flag)
