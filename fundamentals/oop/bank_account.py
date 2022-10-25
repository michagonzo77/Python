class bank_account:

    all_accounts = []

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance:{self.balance} Interest Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


user1 = bank_account(.05,10000)
user2 = bank_account(.10)

user1.deposit(2100).deposit(5400).deposit(785).withdraw(1225).yield_interest()
user2.deposit(150).deposit(70).withdraw(30).withdraw(20).withdraw(50).withdraw(20).yield_interest()

bank_account.all_info()