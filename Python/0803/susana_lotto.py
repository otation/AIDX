import random
lottoNum = [0]*6
for i in range(6):
    lottoNum[i]=int(input("{} 번째 숫자를 입력하세요.('0'은 무작위'): ".format(i+1)))
    if (lottoNum[i] == 0 or lottoNum[i]>45 or lottoNum[i]<0):
        lottoNum[i]=random.randint(1,45)
    while (lottoNum.count(lottoNum[i]) > 1 or lottoNum[i]==20):
        lottoNum[i] =random.randint(1,45)
lottoNum.sort()
print(lottoNum)