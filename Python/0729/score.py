#점수를 입력받아 90점 이상이면 A, 그렇지 않고 80점 이상이면 B,
#그렇지 않고 70점 이상이면 C, 그렇지 않고 60점 이상이면 D,
#그렇지 않으면 F

score = int(input("점수를 입력하세요:"))

if score >= 90:
	print("A 등급")
elif score >= 80:
	print("B 등급")
elif score >= 70:
	print("C 등급")
elif score >= 60:
	print("D 등급")
else:
	print("F 등급")
