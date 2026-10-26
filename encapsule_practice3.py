class Account:
    def __init__(self, balance):
        self.balance = balance


    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            raise ValueError('Balance cannot be negative')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('Cannot deposit negative amount')


    def withdraw(self, amount):
        if amount < 0:
            print('Cannot withdraw negative amount')
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount


account = Account(1000)
print(account.balance)
account.deposit(100)
print(account.balance)
account.withdraw(200)
print(account.balance)
account.withdraw(9000)
print(account.balance)
account.balance = 0
print(account.balance)

