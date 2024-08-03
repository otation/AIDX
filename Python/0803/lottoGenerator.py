import random

#0.변수 설정
lottoNum = [0,0,0,0,0,0]

#1. 입력
for i in range(6):
    lottoNum[i]=int(input("{} 번째 숫자를 입력하세요.('0'은 무작위'): ".format(i+1)))

#2. 입력안한 부분 생성
for i in range(6):
    if lottoNum[i] == 0:
        lottoNum[i]=random.randint(1,45)

    else:
        lottoNum[i] = lottoNum[i]

#3. 중복제거
for i in range(6):
    while lottoNum.count(lottoNum[i]) >= 2:
        lottoNum[i] =random.randint(1,45)

#4. 결과도출
lottoNum.sort()
print(lottoNum)