class Account:

    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'r') as f:
            self.balance = int(f.readline())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filename, 'w') as f:
            f.write(str(self.balance))

acc = Account('oop_bank\\balance.txt')
print(acc.balance)
acc.withdraw(100)
acc.commit()
print(acc.balance)
