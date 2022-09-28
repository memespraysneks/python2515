from xml.dom.minidom import Attr
from customer import Customer


class Account:
    """
    A class that contains multiple useful functions to allow for transfering, withdrawing, 
    and depositing amounts of money as well as containing information to calculate interest.
    """

    def __init__(self, owner, Amount = 0):
        if type(owner) != Customer:
            raise AttributeError
        self.owner = owner
        self.amount = Amount
        self.interest = 0

    def deposit(self, amount):
        """
        Checks to ensure that the amount is greater than 0 as well as it being either a integer or a float
        If not it raises a AttributeError
        """
        if type(amount) not in [int, float] or amount < 0:
            raise AttributeError()
        else:
            self.amount += amount
    
    def withdraw(self, amount):
        """
        Withdraws a certain amount of money from an account
        If the account is a SavingsAccount and the amount being withdrawn is greater than amount stored
        Raises a UserWarning
        Otherwise if ammount is less than 0 or not a integer or a float raise an attribute error
        """
        if type(self) == SavingsAccount and amount > self.amount:
            raise UserWarning()
        if type(amount) not in [int,float] or amount < 0:
            raise AttributeError()
        else:
            self.amount -= amount
    
    def transfer(self, account, amount):
        """
        Ensures that both accounts are of the Account class and then withdraws from one and deposits to the other
        """
        if type(account) == Account:
            self.withdraw(amount)
            account.deposit(amount)
        else:
            raise TypeError()
    
    def compute_interest(self):
        """
        Computes the amount of interest owed on an account if it is negative and the type is credit
        Computes the amount of interest owed on an account regardless of value if it is a savings account
        """ 
        if self.amount < 0 and type(self) == CreditAccount:
            self.amount = self.amount*(100 + self.interest) / 100
            self.amount -= 10
        if type(self) == SavingsAccount:
            self.amount = self.amount*(100 + self.interest) / 100

class CreditAccount(Account):
    """
    Simple class inheriting from Account
    """
    def __init__(self, account, interest):
        super().__init__(account)
        self.interest = interest
    
class SavingsAccount(Account):
    """
    Simple class inheriting from Account
    """
    def __init__(self, account, interest):
        super().__init__(account)
        self.interest = interest