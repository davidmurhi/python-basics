class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}")

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")


account1 = BankAccount("David")
account1.deposit(500)
account1.withdraw(1000)
account1.withdraw(200)
account1.show_balance()
