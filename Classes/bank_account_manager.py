class Account:
    def __init__(self, balance: float):
        assert balance > 0
        self.balance = balance

    def deposit(self, amount: float):
        assert amount > 0
        self.balance += amount
        return f"{amount} is added to your account"

    def withdraw(self, amount: float):
        assert self.balance >= amount > 0
        self.balance -= amount
        return f"{amount} is withdraw to your account"

    def get_amount(self):
        return self.balance


class CheckingAccount(Account):
    pass


class SavingsAccount(Account):
    pass


class BusinessAccount(Account):
    pass

