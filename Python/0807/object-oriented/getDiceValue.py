from random import randint

class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__size = 30
        self.__value = 1
    def getDiceValue(self):
        return self.__value
    def printDice(self):
        print('주사위의 값 = ', self.__value)
    def rollDice(self):
        self.__value = randint(1,6)

dice1 = Dice(100,100)
dice1.rollDice()
dice1.printDice()

    