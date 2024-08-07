class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("도형을 그림")
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    def printArea(self):
        print("원의 면적 =", 3.14 * (self.radius **2))
    def draw(self):
        print("원을 그림")
class Rectangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height
    def printArea(self):
        print("사각형의 면적 =", self.base * self.height)
    def draw(self):
        print("사각형을 그림")
c1 = Circle(5,6,10)
c1.printArea()
c1.draw()