class Account:

    def __init__(self, filename):
        self.filename = filename    # instance variable - self.variablename
        with open(filename, 'r') as f:
            self.balance = int(f.readline())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filename, 'w') as f:
            f.write(str(self.balance))

class Checking(Account):
    """
    doc string - class description, available under __doc__ variable
    """

    type = 'checking' #class variable - shared between all class instaces

    def __init__(self, filename, fee):
        Account.__init__(self, filename)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking('oop_bank\\balance.txt', 1)
checking.transfer(10)
checking.commit()
print(checking.balance)
print(checking.__doc__)
