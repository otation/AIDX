class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withraw_charge = 10000
    def withraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)

class SavingAccount(BankAcount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.interest_rate = 0.03
    def add_interst(self):
        BankAccount.deposit(self, self.balance*(1+self.balance))
