list = [5, 3, 9, 1, 8, 7]
listSquare = []
i = 0

for i in range(6):
    if ((list[i])%2) == 0: 
        listSquare.append(list[i]*list[i])

listSquare.sort()
print(listSquare)