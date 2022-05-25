class BankAccount:
    """
    This class defines a bank account.

    Attributes: checking, savings
    """

    def __init__(self, checking: float = 0., savings: float = 0.):
        self._checking = checking
        self._savings = savings

    def get_checking(self):
        return self._checking

    def get_savings(self):
        return self._savings

    def set_checking(self, new_checking):
        self._checking = new_checking

    checking = property(get_checking, set_checking)

    def set_savings(self, new_savings):
        self._savings = new_savings

    savings = property(get_checking, set_savings)


my_account = BankAccount()

my_account.set_checking(523.48)
print(my_account.get_checking())
my_account.set_savings(386.15)
print(my_account.get_savings())
