class Account:
    def __init__(self, balance):
        self._balance = balance


    @property
    def balance(self):
        return self._balance


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("You cannot deposit negative amounts")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            print("You cannot withdraw negative amounts")


account = Account(1000)
print(account.balance)

account.deposit(100)
print(account.balance)
account.deposit(200)
print(account.balance)
