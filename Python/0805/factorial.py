#재귀함수를 써서 팩토리얼 구하기

def factorialNum(num):
    if num == 1:
        return 1
    else:
        return num * factorialNum(num-1)

inputData = int(input('0보다 큰 숫자를 입력하세요.'))
result = factorialNum(inputData)
print('%d! = %d\n'%(inputData, result))



        