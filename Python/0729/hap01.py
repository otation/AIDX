sumthree = 0
sumnth = 0
for number in range(1,101):

	if number%3==0:
		sumthree = sumthree + number
	else:
		sumnth = sumnth + number

print("3의 배수들의 합 = {}".format(sumthree))
print("3의 배수가 아닌 수들의 합 = {}",format(sumnth))
print("{}+{}={}".format(sumthree, sumnth, (sumthree+sumnth)))
