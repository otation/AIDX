movieRank = ['닥터스트레인지', '스플릿', '럭키']
print(movieRank)


changeMovie=input('바꿀 영화 이름을 입력하세요. :')
num=movieRank.index(changeMovie)
del(movieRank[num])
addMovie=input('추가할 영화 이름을 입력하세요.: ')
movieRank.append(addMovie)
print(movieRank)
