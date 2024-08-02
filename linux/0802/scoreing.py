import statistics

scores=[]
sumScore = 0

for i in range(10):
    scores.append(int(input("{}번 학생점수 입력 : ".format(i+1))))
    sumScore += scores[i]

avg = sumScore/len(scores)
maxScore = max(scores)
minScore = min(scores)

for i in range(10):
    print("{}번 학생의 성적 = {}".format(i+1, scores[i]))

print("성적 합: ", sumScore)
print("성적 평균: ", avg)
print("최고 성적: ",maxScore)
print("최소 성적: ",minScore)

score = int(input("특정 점수 이상의 학생 출력하기"))
cnt = 0
for i in range
