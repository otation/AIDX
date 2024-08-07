class Bank():
    def getInterestRate(self):
        return 0
class BadBank(Bank):
    def getInterestRate(self):
        return 10
class NormalBank(Bank):
    def getInterestRate(self):
        return 5
class GoodBank(Bank):
    def getInterestRate(self):
        return 3

b1 = BadBank()
b2 = NormalBank()
b3 = GoodBank()
print(b1.getInterestRate())
print(b2.getInterestRate())
print(b3.getInterestRate())