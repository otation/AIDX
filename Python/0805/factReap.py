num = int(input('숫자 입력 : '))

fact = 1
for i in range(num,0,-1):
    fact *= i

print("{}! = {}".format(num, fact)) 
