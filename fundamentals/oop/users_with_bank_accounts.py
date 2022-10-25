user1_data = {
    "name": "michael",
    "email": "michael@gmail.com",
    "int_rate": .05}


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
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance} Interest Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

class user:

# Creates User

    def __init__(self, name, email):
        self.name = "name"
        self.email = "email"
        self.accounts = {}

# Creates Bank Account

    def create_account(self, key, int_rate):
        self.accounts[key] = bank_account(int_rate) # Create Key Name in accounts dictionary with value of new bank account from bank_account class init function.
        return self

    def __repr__(self):
        return f"Hello my name is {self.name} and my account number is {self.number}"

    def make_deposit(self, amount, key_name):
        self.accounts[key_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, key_name):
        self.accounts[key_name].withdraw(amount)
        return self

    def display_user_balance(self, key_name):
        self.accounts[key_name].display_account_info()
        return self

    def transfer_money(self, amount, key_name, other_user, key_name2):
        self.accounts[key_name].balance -= amount
        other_user.accounts[key_name2].balance += amount




user1 = user("michael","michael@gmail.com")
user2 = user("joshua","joshua@gmail.com")
user3 = user("luna","luna@gmail.com")

user1.create_account("checkings", .01).create_account("savings",.09).display_user_balance("checkings").display_user_balance("savings")
user2.create_account("checkings", .02).create_account("savings",.07).display_user_balance("checkings").display_user_balance("savings")


























# user1.make_deposit(2100).make_deposit(5400).make_deposit(785).make_withdrawal(1225).display_user_balance()
# user2.make_deposit(150).make_deposit(70).make_withdrawal(30).make_withdrawal(20).make_withdrawal(50).make_withdrawal(20).display_user_balance()

# user1.display_user_balance("checkings")
# user2.display_user_balance("checkings")
# user3.display_user_balance("checkings")

# user1.display_user_balance("savings")
# user2.display_user_balance("savings")
# user3.display_user_balance("checkings")
# user3.display_user_balance("savings")

# user3.make_withdrawal(25000,"checkings")

# user3.display_user_balance("checkings")
# user3.display_user_balance("savings")

# user2.display_user_balance("checkings")
# user2.display_user_balance("savings")

# user3.transfer_money(15000, "checkings", user2, "checkings")

# user3.display_user_balance("checkings")
# user3.display_user_balance("savings")

# user2.display_user_balance("checkings")
# user2.display_user_balance("savings")


# print(bank_account.all_balances())

# user1.display_user_balance("checkings")
# user2.display_user_balance("checkings")
# user3.display_user_balance("checkings")

# user1.display_user_balance("savings")
# user2.display_user_balance("savings")
# user3.display_user_balance("savings")


# self.accounts = {
#     "checking": bank_account(int_rate, balance),
#     "savings": bank_account(int_rate, balance)
# }

# self.accounts[checking].deposit(amount)

# if a list append to that list
# if a dict append to the dictionary with key and value pair

# def __init__(self, name, email, int_rate, balance = 0):
#     self.name = name
#     self.email = email
#     self.accounts = {
#         "checkings": bank_account(int_rate, balance),
#         "savings": bank_account(int_rate, balance)
#     }
# if act_num not in all_accounts:
#     self.act_num = random.randrage(999999)



# def __init__(self, name, email, int_rate, balance = 0):
#     self.name = name
#     self.email = email
#     self.accounts = {
#         "checkings": bank_account(int_rate, balance),
#         "savings": bank_account(int_rate, balance)
#     }
# if act_num not in all_accounts:
#     self.act_num = random.randrage(999999)


# self.accounts.append(bank_account(int_rate, balance))


# print(self.user_accounts)
# for key_name in user_accounts:
#     key_name.display_account_info()
# return self


# def open_account(self, key, int_rate):
#     self.account[key] = bankaccount(int_rate)
#     return self

# self.accounts[key_name].withdraw(amount)
# other_user.accounts[key_name2].deposit(amount)