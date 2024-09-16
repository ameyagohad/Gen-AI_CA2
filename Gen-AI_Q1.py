import random

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('Deposit', amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(('Withdraw', amount))
        else:
            self.transactions.append(('Withdraw', 0))

    def get_balance(self):
        return self.balance

    def print_account_summary(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

def generate_accounts(num_accounts, months, num_transactions_per_month, seed_value):
    random.seed(seed_value)
    accounts = []

    for i in range(num_accounts):
        initial_balance = round(random.uniform(1000, 10000), 2)
        account = BankAccount(f"ACCT-{i+1}", initial_balance)

        for month in range(months):
            for _ in range(num_transactions_per_month):
                transaction_type = random.choice(['deposit', 'withdrawal'])
                amount = round(random.uniform(100, 1000), 2)

                if transaction_type == 'deposit':
                    account.deposit(amount)
                elif transaction_type == 'withdrawal':
                    account.withdraw(amount)

        accounts.append(account)

    return accounts

def print_sorted_accounts(accounts):
    sorted_accounts = sorted(accounts, key=lambda acc: acc.get_balance())

    print("\nAccounts Sorted by Balance (Lowest to Highest):")
    for account in sorted_accounts:
        account.print_account_summary()

num_accounts = 100
months = 6
num_transactions_per_month = 10
seed_value = 42

accounts = generate_accounts(num_accounts, months, num_transactions_per_month, seed_value)

print_sorted_accounts(accounts)
