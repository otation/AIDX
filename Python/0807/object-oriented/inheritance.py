class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self, make):
        self.make = make
    def getMake(self):
        return self.make
    def printInfo(self):
        return self.make + self.model + self.color + str(self.price)

class ElectricCar(car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize
    def setBatterySize(self, batterySize):
        self.batterySzie = batterySize
    def getBatterSize(self):
        return self.batterySize
    def printInfoElec(self):
        return super().printInfo() + str(self.batterySize)

def main():
    myCar = car("HD", "Avante", "black", 2000000, 0)
    print(basicCar.printInfo())
    myCar.setMake("Tesla")

