import random
from datetime import datetime
from pickle import FALSE


class Bank:
    def __init__(self, name_of_bank="Best Of The Best Bank", users_of_bank = None, accounts_of_bank = None):
        self.name = name_of_bank
        self.users = users_of_bank if users_of_bank is not None else {}
        self.accounts = accounts_of_bank if accounts_of_bank is not None else {}



class Client:
    def __init__(self, id, name="Bob", accounts_by_currency=None):
        self.id = id if id is not None else random.randint(1, 1000000) #если не ввели id то автоматом делаем id, в нашем банке до 1.000.000 пользователей
        self.name = name
        self.accounts_by_currency = accounts_by_currency if accounts_by_currency is not None else {}



class BankAccount:
    def __init__(self, id=None, owner_id=None, currency="BYN", balance=0.0, open_date=None):

        if owner_id is None:
            raise Exception("Не может быть счёта без владельца, нужны данные id владельца")

        self.id = id if id is not None else random.randint(1, 1000000)
        self.owner_id = owner_id
        self.currency = currency
        self.balance = balance
        self.open_date = open_date if open_date is not None else datetime.now()

    def deposit(self, amount):
        if amount < 0:
            raise Exception("Нельзя пополнить на отрицательное число")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Недостаточно валюты на балансе")
        if amount < 0:
            raise Exception("Нельзя выводить отрицательное число")
        self.balance -= amount
