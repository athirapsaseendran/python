class BankAccount:

    def __init__(self, account_number, account_holder, account_type, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Account Type:", self.account_type)
        print("Current Balance:", self.balance)


account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")
account_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder, account_type, balance)

account.display()

deposit_amount = float(input("\nEnter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.display()
