class BankAccount:
    def __init__(self):
        self.name = "Hong"
        self.__balance = 0
    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에서", amount, "가 출금되었습니다.")
        print("잔액은 ", self.__balance, "입니다.")
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print("통장에 ", amount, "를 입금하였습니다.")
        print("잔액은 ", self.__balance, "입니다.")
        return self.__balance

cus1 = BankAccount()
cus1.deposit(100)
cus1.withdraw(500)