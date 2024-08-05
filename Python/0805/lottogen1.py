#로또번호 생성기 1~45번 정수 중 중복 없는 6개 선택
#1~6개 중 원하는 번호 입력가능 나머지는 자동 선택
#싫어하는 번호 입력가능

import random

lottoNum = [0,0,0,0,0,0]
hateNum = []
hateNum.append(input("자동선택에 제외할 번호를 입력하세요. :"))

for i in range(6):
    lottoNum[i] = int(input("{}번째 숫자를 입력하세요. 0 을 입력하면 자동 선택".format[i]))
    hateNum
    if lottoNum[i] == 0:
        lottoNum[i] = random.randint(1,45)
    else:
        lottoNum[i] = lottoNum[i]
    while (lottoNum.count[lottoNum(i)] > 1) or (hateNum.count[lottoNum(i)] > 0):
        lottoNum[i] = random.randint(1,45)

        