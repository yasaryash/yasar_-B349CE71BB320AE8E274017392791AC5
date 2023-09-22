class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: {self.__account_balance}")

# Create an instance of BankAccount
account = BankAccount("1234567890", "John Doe", 1000)

# Test deposit and withdrawal
account.deposit(500)
account.display_balance()  # Output: Account Balance: 1500

account.withdraw(200)
account.display_balance()  # Output: Account Balance: 1300

account.withdraw(1500) # Output: Insufficient funds!
