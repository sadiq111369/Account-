from account import Account


class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdraw_limit = 100

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied. New balance: ${self.get_balance()}")

    def withdraw(self, amount):
        """Override withdrawal to enforce the $100 withdrawal limit."""
        if amount > self.withdraw_limit:
            print(f"Withdrawal amount exceeds limit of ${self.withdraw_limit}. Cannot withdraw ${amount}.")
        elif 0 < amount <= self.withdraw_limit:
            if amount <= self.get_balance():
                self._balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.get_balance()}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")


print("--- Savings Account ---")
savings = Savings("Alice", 1000)
print(f"Initial balance: {savings.get_balance()}")

savings.deposit(500)
savings.withdraw(200)
savings.apply_interest()