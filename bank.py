import random
from datetime import datetime
import json


class Bank:
    def __init__(self, name_of_bank="Best Of The Best Bank", users_of_bank = None, accounts_of_bank = None):
        self.name = name_of_bank
        self.users = users_of_bank if users_of_bank is not None else {}
        self.accounts = accounts_of_bank if accounts_of_bank is not None else {}

    def create_account(self, name):
        while True:
            client_id = random.randint(1, 1000000)
            if client_id not in self.users:
                break

        new_client = Client(client_id, name)
        self.users[client_id] = new_client
        return client_id

    def open_account(self, client_id, currency="BYN"):
        if client_id not in self.users:
            raise Exception("Клиента не сущетсвует (id)")
        client = self.users[client_id]

        if currency in client.accounts_by_currency:
            raise Exception("В такой валюте счёт уже существует")

        while True:
            bank_account_id = random.randint(1, 1000000)
            if bank_account_id not in self.accounts:
                break

        bank_account = BankAccount(bank_account_id, client_id, currency)
        self.accounts[bank_account_id] = bank_account
        client.accounts_by_currency[currency] = bank_account.id
        return bank_account.id

    def close_account(self, client_id, account_id):
        if client_id not in self.users:
            raise Exception("Нет пользователя с таким id")

        client = self.users[client_id]

        if account_id not in self.accounts:
            raise Exception("Нет счёта с таким id")

        bank_account = self.accounts[account_id]
        if bank_account.owner_id != client_id:
            raise Exception("Нет такого счёта у пользователя с таким id")
        if bank_account.balance != 0:
            raise Exception(f"Баланс не равен нулю, снимите сначала деньги со счёта (баланс счёта {bank_account.balance}, {bank_account.currency})")

        del self.accounts[account_id]
        del client.accounts_by_currency[bank_account.currency]

    def deposit(self, client_id, account_id, amount):
        if client_id not in self.users:
            raise Exception("Клиент с таким ID не найден")
        client = self.users[client_id]

        if account_id not in self.accounts:
            raise Exception("Счет с таким ID не найден")
        account = self.accounts[account_id]

        if account.owner_id != client_id:
            raise Exception("Клиент не является владельцем счета")

        account.deposit(amount)
        print(f"Счет {account_id} успешно пополнен на {amount} {account.currency}. Новый баланс: {account.balance} {account.currency}")

    def withdraw(self, client_id, account_id, amount):
        if client_id not in self.users:
            raise Exception("Клиент с таким ID не найден")
        client = self.users[client_id]

        if account_id not in self.accounts:
            raise Exception("Счет с таким ID не найден")
        account = self.accounts[account_id]

        if account.owner_id != client_id:
            raise Exception("Клиент не является владельцем счета")

        account.withdraw(amount)

        print(f"Со счета {account_id} снято {amount} {account.currency}. Новый баланс: {account.balance} {account.currency}")

    def transfer(self, client_id, from_account_id, to_account_id, amount):
        if client_id not in self.users:
            raise Exception("Клиент с таким ID не найден")
        client = self.users[client_id]

        if from_account_id not in self.accounts:
            raise Exception("Исходный счет не найден")
        from_account = self.accounts[from_account_id]

        if from_account.owner_id != client_id:
            raise Exception("Клиент не является владельцем исходного счета")

        if to_account_id not in self.accounts:
            raise Exception("Целевой счет не найден")
        to_account = self.accounts[to_account_id]

        if from_account.currency != to_account.currency:
            raise Exception("Валюты счетов не совпадают")

        if amount <= 0:
            raise Exception("Сумма перевода должна быть больше нуля")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Перевод {amount} {from_account.currency} выполнен с счета {from_account_id} на счет {to_account_id}")

    def get_statement(self, client_id):
        if client_id not in self.users:
            raise Exception("Клиент с таким ID не найден")
        client = self.users[client_id]

        statement = {
            "client_id": client.id,
            "client_name": client.name,
            "accounts": [],
            "total_balances": {}
        }

        for currency, account_id in client.accounts_by_currency.items():
            account = self.accounts[account_id]
            statement["accounts"].append({
                "account_id": account.id,
                "currency": account.currency,
                "balance": account.balance,
                "open_date": account.open_date.isoformat()
            })

            if account.currency in statement["total_balances"]:
                statement["total_balances"][account.currency] += account.balance
            else:
                statement["total_balances"][account.currency] = account.balance

        filename = f"statement_{client.id}.json"
        with open(filename, "w") as f:
            json.dump(statement, f, indent=4)

        print(f"Выписка сохранена в файл {filename}")
        return statement

    def save_to_file(self, filename = "bank_data.json"):
        data = {"name" : self.name, "users" : {}, "accounts": {}}
        for client_id, client in self.users.items():
            data["users"][client_id] = {
                "id": client.id,
                "name": client.name,
                "accounts_by_currency": client.accounts_by_currency
            }

        for account_id, account in self.accounts.items():
            data["accounts"][account_id] = {
                "id": account.id,
                "owner_id": account.owner_id,
                "currency": account.currency,
                "balance": account.balance,
                "open_date": account.open_date.isoformat()
            }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Банк сохранен в файл {filename}")

    def load_from_file(self, filename="bank_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.name = data["name"]
            self.users = {}
            self.accounts = {}

            for client_id, client_data in data["users"].items():
                self.users[int(client_id)] = Client(
                    id=int(client_data["id"]),
                    name=client_data["name"],
                    accounts_by_currency=client_data["accounts_by_currency"]
                )

            for account_id, account_data in data["accounts"].items():
                self.accounts[int(account_id)] = BankAccount(
                    id=int(account_data["id"]),
                    owner_id=int(account_data["owner_id"]),
                    currency=account_data["currency"],
                    balance=account_data["balance"],
                    open_date=datetime.fromisoformat(account_data["open_date"])
                )
            print(f"Банк загружен из файла {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создан новый банк.")


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

def run_bank_interface(bank):
    print(f"Добро пожаловать в {bank.name}!\n")

    while True:
        try:
            print("\nМеню:")
            print("1. Создать нового клиента")
            print("2. Открыть счет")
            print("3. Закрыть счет")
            print("4. Пополнить счет")
            print("5. Снять деньги со счета")
            print("6. Перевести деньги")
            print("7. Получить выписку")
            print("0. Выход")

            choice = input("Выберите действие: ")

            if choice == "0":
                print("Выход из программы...")
                break

            elif choice == "1":
                name = input("Введите имя клиента: ")
                client_id = bank.create_account(name)
                print(f"Клиент создан с ID: {client_id}")

            elif choice == "2":
                client_id = int(input("Введите ваш ID: "))
                currency = input("Введите валюту (например, BYN, USD): ")
                account_id = bank.open_account(client_id, currency)
                print(f"Счет открыт ID счета: {account_id}")

            elif choice == "3":
                client_id = int(input("Введите ваш ID: "))
                account_id = int(input("Введите ID счета для закрытия: "))
                bank.close_account(client_id, account_id)
                print("Счет успешно закрыт")

            elif choice == "4":
                client_id = int(input("Введите ваш ID: "))
                account_id = int(input("Введите ID счета для пополнения: "))
                amount = float(input("Введите сумму для пополнения: "))
                bank.deposit(client_id, account_id, amount)

            elif choice == "5":
                client_id = int(input("Введите ваш ID: "))
                account_id = int(input("Введите ID счета для снятия: "))
                amount = float(input("Введите сумму для снятия: "))
                bank.withdraw(client_id, account_id, amount)

            elif choice == "6":
                client_id = int(input("Введите ваш ID: "))
                from_id = int(input("Введите ID исходного счета: "))
                to_id = int(input("Введите ID целевого счета: "))
                amount = float(input("Введите сумму для перевода: "))
                bank.transfer(client_id, from_id, to_id, amount)

            elif choice == "7":
                client_id = int(input("Введите ваш ID: "))
                bank.get_statement(client_id)

            else:
                print("Неверный выбор. Попробуйте снова.")

        except Exception as error_info:
            print("Ошибка:", error_info)

my_bank = Bank()
my_bank.load_from_file()
run_bank_interface(my_bank)
my_bank.save_to_file()
