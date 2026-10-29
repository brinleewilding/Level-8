import random


class BankAccount:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.account_number = random.randint(10000,99999)
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
