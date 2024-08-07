class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age
    def getAge(self):
        return self.__name
    
obj = Student("Hong", 50)
print(obj.getAge())
