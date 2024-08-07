

class Counter:
    def __init__(self):
        self.count = 0
    def increament(self):
        self.count +=1

a = Counter()
b = Counter()
c = Counter()
d = Counter()

a.increament()
a.increament()
print(a.count)

d.count = 0
d.count += 1
d.count += 1
d.count += 1
print(d.count)