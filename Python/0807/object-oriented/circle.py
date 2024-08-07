import math

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
circle1 = Circle(10)
print('원의 면적 : ', circle1.getArea())
print('원의 둘레 : ', circle1.getPerimeter())

circle2 = Circle()
circle2.setRadius(int(input("원의 지름 입력 : ")))
print('원의 면적 : ', circle2.getArea())
print('원의 둘레 : ', circle2.getPerimeter())
