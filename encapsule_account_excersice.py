class Account:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("You cannot initialize negative amounts")
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("You cannot deposit negative amounts")


    def withdraw(self, amount):
        if amount <= 0:
            print("Cannot withdraw negative amounts")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount



    def get_balance(self):
        return self.__balance


account = Account(1000)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
account.withdraw(900)
print(account.get_balance())
