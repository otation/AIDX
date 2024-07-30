quota=int(input("나눠줄 빵 갯수를 쓰세요.:"))

breadTotal=97
person=breadTotal//quota
left=breadTotal%quota

print("나눠줄 수 있는 사람의 수는",person)
print("남은 빵의 수는",left)

