class Vertor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vertor2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vertor2D(self.x - other.x, self.y + other.y)
    def __eq__(self, other):
        return Vertor2D(self.x == other.x, self.y + other.y)
    def __str__(self):
        return '(%g, %g)'%(self.x, self.y)

u = Vertor2D(0,1)
v = Vertor2D(1,0)
w = Vertor2D(1,1)
a = u + v + w

print(a)