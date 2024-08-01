scores = [55, 35, 40, 70, 65, 30]

total = 0
underSubject = 0
average = 0

for score in scores:
    if score < 40:
        underSubject += 1
    total += score

print('40점 미만 과목 수 : ', underSubject)
average = total / len(scores)
print('평균 점수 : ', average)

if underSubject > 0 or average < 60:
    print('불합격입니다.')
else:
    print('합격입니다.')
    
