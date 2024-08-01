toDoList = ['cleaning', 'shooping', 'TOEIC study', 'exercise']
print('오늘의 할 일 : ', toDoList)

for i in range(len(toDoList)):
    print('끝난 일 :', toDoList.pop(0))
    if len(toDoList) != 0:
        print('남은 일 :', toDoList)
    else:
        print('할 일 끝!')
        