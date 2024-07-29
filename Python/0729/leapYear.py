#윤년은 4의 배수이고 100의 배수는 아니고 400의 배수이면 윤년입니다.
#년도를 입력받아 윤년인지 평년(common year)인지를 출력하는 프로그램을 작성하세요.

year = int(input("년도 입력:"))

if year%4 == 0 and year%100 != 0 or year%400 == 0:
	print("윤년(leap year)입니다.")

else:
	print("평년(common year)입니다.")
