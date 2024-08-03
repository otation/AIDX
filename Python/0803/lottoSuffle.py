import random as rn
#1~45 number create
lottoNum = list(range(1, 46))
#print(lottoNum)

#shuffle list
rn.shuffle(lottoNum)
#print(lottoNum)

#user input wait
#must input 0~6 and break while
print("How many you want auto lotto number?(manual=0 ~ full auto=6) : ")
while True:
    howMany = int(input("enter the auto number(0~6) : "))
    #while 0~6 loop
    if 0 <= howMany and howMany <= 6:
        #if 0~6, break
        break
    else:
        print("manual=0 ~ full auto=6")

#define my num list
myNum=[]
#auto pop lotto number
for i in range(howMany):
    myNum.append(lottoNum.pop())

#manual input and delete duplication
for i in range(6-howMany):
    manual = int(input("enter the manual number : "))
    #if no duplicated, append and remove
    if myNum.count(manual) == 0:
        myNum.append(manual)
        lottoNum.remove(manual)
    #if duplicated, pick up random number
    else:
        print("duplicated! random number is selected")
        myNum.append(lottoNum.pop())

#sort and show
myNum.sort()
print("my lotto numbers are : ", myNum)