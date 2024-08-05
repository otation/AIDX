
def calculator(num1, num2):
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2

    return [result1, result2, result3, result4]

inputNumber1 = int(input('첫 번째 정수 입력 :'))
inputNumber2 = int(input('두 번째 정수 입력 :'))

result = calculator(inputNumber1, inputNumber2)
print(type(result))
print('사칙 연산 결과 :',result)
print('덧셈 :',result[0])
print('뺄셈 :',result[1])
print('곱셈 :',result[2])
print('나눗셈 :',result[3])
