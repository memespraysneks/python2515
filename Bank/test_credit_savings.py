import pytest

from account import Account, CreditAccount, SavingsAccount
from customer import Customer

@pytest.fixture
def tim():
    """Tim is a regular customer"""
    return Customer("Tim", "142904328")

@pytest.fixture
def credit10(tim):
    """Credit account with 10% interest"""
    return CreditAccount(tim, 10)

@pytest.fixture
def savings5(tim):
    """Savings account with 5% interest"""
    return SavingsAccount(tim, 5)

def test_inheritance(credit10, savings5):
    """Check attributes and inheritance of instances"""
    assert isinstance(credit10, Account)
    assert isinstance(savings5, Account)

    assert credit10.interest == 10
    assert savings5.interest == 5

def test_credit_interest(credit10):
    """Interest is only charged on a credit account when the amount is negative"""
    credit10.withdraw(500)
    assert credit10.amount == -500

    credit10.compute_interest()
    assert credit10.amount == -560

    credit10.deposit(1000)
    credit10.compute_interest()
    assert credit10.amount == 440

def test_savings_interest(savings5):
    """Check savings interest"""
    savings5.deposit(1000)
    savings5.compute_interest()
    assert savings5.amount == 1050

def test_savings_withdraw(savings5):
    """Check you cannot go below 0 on a savings account"""
    savings5.deposit(500)
    with pytest.raises(UserWarning):
        savings5.withdraw(1000)

    assert savings5.amount == 500