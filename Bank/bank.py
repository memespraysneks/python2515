from account import Account, SavingsAccount, CreditAccount

class Bank:
    """Creates a class instance with an empty account list"""
    def __init__(self, name):
        self.name = name
        self._accounts = []


    @property
    def accounts(self):
        print("getter method called")
        return self._accounts

    
    @accounts.setter
    def accounts(self, account):
        print("setter method called")
        self._accounts.append(account)

    def create_account(self, category, owner, interest_rate = 0):
        """Creates an account of the specified type, if the type is not in the list of possibilities
        an AttributeError will be raised"""

        if category not in ["account", "credit", "savings"]:
            raise AttributeError()
        elif category == "account":
            self.accounts = Account(owner)
            return self.accounts[-1]
        elif category == "credit":
            self.accounts = CreditAccount(owner, interest_rate)
            return self.accounts[-1]
        else:
            self.accounts = SavingsAccount(owner, interest_rate)
            return self.accounts[-1]
    
    def compute_interest(self):
        """Computes the interest of all accounts (even if accounts interest rate is 0)"""

        for account in self.accounts:
            account.compute_interest()

    def find_accounts(self, name):
        """Finds all accounts with a given name as the owner and returns a list of all of these accounts."""
        account_list = []
        for account in self.accounts:
            if account.owner.name == name:
                account_list.append(account)
        return account_list