def printAverageScore(*scores):
    print(type(scores))

    totalScore = 0
    cnt = len(scores)

    for score in scores:
        totalScore += score
        
    print('총점 : ',totalScore,'점')
    print('평점 : ',totalScore/cnt,'점')
    print('-------------')

printAverageScore(80, 90, 100)
printAverageScore(90, 85, 90, 99)
printAverageScore(95, 100, 100, 97, 88)