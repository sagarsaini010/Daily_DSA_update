class InsufficientBalance(Exception):
    def __init__(self, errmsg):
        self.errmsg = errmsg

    def __str__(self):
        return self.errmsg

    def __repr__(self):
        return f"InsufficientBalance('{self.errmsg}')"


class Account:
    def __init__(self,accno,bal):
        self.accno = accno
        self.bal = bal

    def showBalance(self):
        print(self.bal)

    def withdraw(self,amt):
        if self.bal < amt:
            raise InsufficientBalance("Balance to low")
        self.bal = self.bal - amt
        print("your have withdraw ",amt)


my_account = Account(100,5000)

my_account.showBalance()
try:
    my_account.withdraw(7000)
except InsufficientBalance as e:
    print(repr(e))

my_account.showBalance()