class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (encapsulated)

    # access the private attribute balance
    def get_balance(self):
        return self.__balance

    # Setter method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Setter method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Create a BankAccount object
ac0001 = BankAccount("Alice", 1000)

# Access the balance through getter
print(f"Initial Balance: ${ac0001.get_balance()}")

# Deposit money
ac0001.deposit(500)

# Withdraw money
ac0001.withdraw(200)

# Try to access the private attribute directly (will raise an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError


# Access the balance after transactions
print(f"Final Balance: ${ac0001.get_balance()}")
